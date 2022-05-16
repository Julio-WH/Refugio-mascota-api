from rest_framework import status, permissions, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from app.API.serializers import MascotasSerializer, PersonaSerializer
from app.mascota.models import Mascota
from rest_framework.response import Response
from django.http import Http404

@api_view(['GET','POST'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAdminUser])
def list_mascotas(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all().order_by("-fecha_rescate")
        mascotas_json = MascotasSerializer(mascotas, many=True)
        return Response(mascotas_json.data)
    elif request.method == 'POST':
        mascotas_json = MascotasSerializer(data=request.data, partial=True)
        if mascotas_json.is_valid():
            mascotas_json.save()
            return Response(mascotas_json.data, status=status.HTTP_201_CREATED)
        return Response(mascotas_json.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAdminUser])
def detail_mascota(request, pk):
    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = MascotasSerializer(mascota)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = MascotasSerializer(mascota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAdminUser])
def mascota_persona_list(request, pk):
    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        persona = mascota.persona
        if persona is not None:
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        raise