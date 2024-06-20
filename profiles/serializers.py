from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Create a ProfileSerializer class 
    Inherit from ModelSerializer and specify owner as a readonly field so it can't be edited
    """

    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'first_name',
            'last_name', 'image', 
        ]