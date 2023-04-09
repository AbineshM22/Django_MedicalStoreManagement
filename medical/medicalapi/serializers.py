from projectapp1.models import Medicalstore
from rest_framework import serializers

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicalstore
        fields ="__all__"