from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from metal_ops.models import ArchivoAdjunto, OrdenTrabajo
from metal_ops.serializers import ArchivoAdjuntoSerializer
from metal_ops.permissions import IsAtencion, ORPermission, IsPlanner

class SubirArchivoOTView(APIView):
    """
    Sube un archivo a una OT y cambia su estado de SIN DISEÑO a SIN FLUJO
    """
    permission_classes = [ORPermission(IsAtencion, IsPlanner)]
    
    def post(self, request, id_ot):
        try:
            # Verificar que la OT existe
            orden = OrdenTrabajo.objects.get(id_ot=id_ot)
            
            # Verificar que viene un archivo
            if 'archivo' not in request.FILES:
                return Response(
                    {"error": "Debes enviar un archivo"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            archivo = request.FILES['archivo']
            
            # Validar extensión
            extensiones_permitidas = ['pdf', 'png', 'jpg', 'jpeg']
            ext = archivo.name.split('.')[-1].lower()
            if ext not in extensiones_permitidas:
                return Response(
                    {"error": f"Solo se permiten archivos: {', '.join(extensiones_permitidas)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Crear el archivo adjunto
            archivo_adjunto = ArchivoAdjunto.objects.create(
                orden_trabajo=orden,
                archivo=archivo,
                descripcion=request.data.get('descripcion', '')
            )
            
            # 🆕 Cambiar estado de SIN DISEÑO a SIN FLUJO si aplica
            if orden.estado_ot == 'SIN DISEÑO':
                orden.estado_ot = 'SIN FLUJO'
                orden.save()
            
            return Response({
                "message": "Archivo subido exitosamente",
                "id_archivo": archivo_adjunto.id_archivo,
                "nuevo_estado": orden.estado_ot
            }, status=status.HTTP_201_CREATED)
            
        except OrdenTrabajo.DoesNotExist:
            return Response(
                {"error": "Orden de trabajo no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ListarArchivosOTView(generics.ListAPIView):
    """
    Lista los archivos de una OT específica
    """
    serializer_class = ArchivoAdjuntoSerializer
    permission_classes = [ORPermission(IsAtencion, IsPlanner)]
    
    def get_queryset(self):
        id_ot = self.kwargs['id_ot']
        return ArchivoAdjunto.objects.filter(orden_trabajo_id=id_ot)