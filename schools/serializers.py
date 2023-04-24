from rest_framework import serializers
from schools.models import Schools

class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schools
        fields=('id' ,'name','email','address','phone')