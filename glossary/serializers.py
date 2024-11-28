from rest_framework import serializers

from glossary.models import Glossary

class Glossaryserializer(serializers.ModelSerializer):
    class Meta:
        model=Glossary
        fields='__all__'