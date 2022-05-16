from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import authentication, generics, permissions
from rest_framework.response import Response

from app.API.serializers import MascotasSerializer, PersonaSerializer
from app.mascota.models import Mascota


class MascotaListGeneric(generics.ListCreateAPIView):

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Mascota.objects.all().order_by("-fecha_rescate")
    serializer_class = MascotasSerializer


class MascotaDetailsGeneric(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Mascota.objects.all()
    serializer_class = MascotasSerializer

class MascotaPersonaListGeneric(generics.RetrieveAPIView):

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        mascota = get_object_or_404(Mascota, pk=self.kwargs.get('pk'))
        persona = mascota.persona
        if persona is not None:
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        raise Http404