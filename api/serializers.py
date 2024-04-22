from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        } 

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("The passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)


    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('A user with this email and password is not found.')

        return data

    def get_object(self):
        return User.objects.filter(email=self.data.get('email')).first()
