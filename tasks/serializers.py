from rest_framework import serializers
from tasks.models import New_task


class NewTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_task
        fields = '__all__'
