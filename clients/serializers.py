from rest_framework import serializers
from clients.models import Client

class ClientSerializer(serializers.ModelSerializer):
    projects = serializers.StringRelatedField(many=True,read_only=True)    
    no_of_projects = serializers.IntegerField(default=0,allow_null=True)
    total_income = serializers.FloatField(default=0,allow_null=True)
    class Meta:
        model = Client
        fields = ('id','company_name','email','phone_number','company_name','company_city','no_of_projects','total_income','projects')



