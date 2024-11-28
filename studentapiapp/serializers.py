from rest_framework import serializers

from studentapiapp.models import StudentAPI
class studentserializer(serializers.ModelSerializer):
    
    class Meta:
        model=StudentAPI
        fields='__all__'
        