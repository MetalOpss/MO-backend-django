# MetalOps Backend (Django)

Este proyecto es un **servicio Django** que valida tokens JWT generados por el backend de Spring Boot.  
El objetivo es permitir la integración entre ambos servicios con autenticación segura.

---

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/) (opcional pero recomendado)
- Acceso a las variables de entorno (`.env`) que se deben configurar manualmente

---

## Instalación y configuración

1. **Clonar el repositorio**

   ```bash
   git clone <URL_DEL_REPO>
   cd <NOMBRE_DEL_REPO>
   ```

2. **Crear y activar un entorno virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/MacOS
   venv\Scripts\activate      # En Windows
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**

   Copiar el archivo de ejemplo:

   ```bash
   cp .env.example .env
   ```

   Editar `.env` con tus credenciales reales (no lo subas a GitHub):

   ```env
   DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DB_NAME
   JWT_SECRET=your_secret_key_here
   ```

---

## Ejecución

1. **Aplicar migraciones**

   ```bash
   python manage.py migrate
   ```

2. **Levantar el servidor de desarrollo**

   ```bash
   python manage.py runserver
   ```

   El servicio estará disponible en:

   ```
   http://127.0.0.1:8000/
   ```

---

## Autenticación

Este proyecto no genera tokens propios, sino que valida los tokens emitidos por el servicio de Spring Boot.

- Los tokens deben estar firmados con **HS512**.
- Se validan contra la clave (`JWT_SECRET`) definida en el `.env`.

**Ejemplo de cabecera en una petición:**

```
Authorization: Bearer <token_generado_en_springboot>
```

---

## Notas importantes

- El archivo `.env` **no se sube al repositorio**.
- Existe un archivo `.env.example` con las variables necesarias para configurar tu entorno.
- Si necesitas nuevas dependencias, instálalas con:
  ```bash
  pip install <paquete>
  ```
  y luego actualiza `requirements.txt`:
  ```bash
  pip freeze > requirements.txt
  ```
