from rest_framework import serializers
from api.models.LaunchpadModels import Launchpads


class LaunchpadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launchpads
        fields = '__all__'
