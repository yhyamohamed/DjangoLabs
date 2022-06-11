from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)


    class Meta:
        fields = ('username', 'email', 'first_name', 'password', 'password_confirmation','date_of_birth')
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'email':{'required':True},
            'date_of_birth':{'required':True},
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username')
        )
        if self.validated_data.get('password') != self.validated_data.get('password_confirmation'):
            raise serializers.ValidationError('pass dont match')

        user.set_password(self.validated_data.get('password'))
        user.save()
        return user
