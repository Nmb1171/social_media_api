from rest_framework import serializers
from django.contrib.auth import get_user_model



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)



User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data['username'],
                email = validated_data['email'],
                password = validated_data['password'],
                bio = validated_data.get('bio', ''),
                profile_picture = validated_data.get('profile_picture', None)
            )

            return user 
        



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile_picture']


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_picture']
