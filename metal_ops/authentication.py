# metal_ops/authentication.py
import os
import base64
import jwt
from types import SimpleNamespace
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class RemoteUser(SimpleNamespace):
    is_authenticated = True


class SpringJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        token = auth_header.split(" ", 1)[1].strip()
        secret_env = os.environ.get("JWT_SECRET")

        if not secret_env:
            raise AuthenticationFailed("JWT_SECRET no configurada en el servidor")

        try:
            key_bytes = base64.b64decode(secret_env)
            
            payload = jwt.decode(
                token, 
                key_bytes, 
                algorithms=["HS512"], 
                options={
                    "verify_signature": True,
                    "verify_exp": True,
                    "verify_nbf": False,
                    "verify_iat": False,
                    "verify_aud": False
                }
            )
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expirado")
        except jwt.InvalidTokenError as e:
            raise AuthenticationFailed("Token inválido")
        except Exception as e:
            raise AuthenticationFailed("Error al procesar el token")

        user = RemoteUser(**payload)
        return (user, payload)