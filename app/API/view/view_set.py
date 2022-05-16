from rest_framework import authentication, permissions, viewsets, status
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.response import Response

from app.API.serializers import MascotasSerializer, PersonaSerializer
from app.mascota.models import Mascota

from django.shortcuts import get_object_or_404


class MascotaViewset(viewsets.ViewSet):

    @authentication_classes([authentication.SessionAuthentication])
    @permission_classes([permissions.IsAdminUser])

    def list(self, request):
        queryset = Mascota.objects.all().order_by("-fecha_rescate")
        serializer = MascotasSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MascotasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        mascota = get_object_or_404(Mascota, pk=pk)
        serializer = MascotasSerializer(mascota)
        return Response(serializer.data)

    def update(self, request, pk=None):
        mascota = get_object_or_404(Mascota, pk=pk)
        serializer = MascotasSerializer(mascota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def persona(self, request, pk=None):
        mascota = get_object_or_404(Mascota, pk=pk)
        persona = mascota.persona
        if persona is not None:
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        raise


# class MascotaPersonaViewset(viewsets.ViewSet):
#
#     def retrieve(self, request, pk=None):
#         mascota = get_object_or_404(Mascota, pk=pk)
#         serializer = PersonaSerializer(mascota.persona)
#         return Response(serializer.data)
