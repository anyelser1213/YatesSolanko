from dataclasses import fields
from rest_framework import serializers
from aplicaciones.usuarios.models import Usuarios


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        #fields = '__all__'
        fields = ['status'] #cuando son campos especificos
        
        #exclude