from rest_framework import serializers
from app.mascota.models import Mascota, Vacuna
from app.adopcion.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id',
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio',)


class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = [
            'id',
            'nombre',
        ]

class MascotasSerializer(serializers.ModelSerializer):
    # persona = PersonaSerializer()
    class Meta:
        model = Mascota
        fields = (
            'id',
            # 'image',
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        )

    def to_representation(self, instance):
        values = super(MascotasSerializer, self).to_representation(instance)
        if values['persona'] is not None: values['persona'] = PersonaSerializer(instance.persona).data
        values['vacuna'] = VacunaSerializer(instance.vacuna, many=True).data
        return  values