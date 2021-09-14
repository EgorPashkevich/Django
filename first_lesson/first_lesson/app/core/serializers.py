from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password',
        ]


def to_representation(self, instance):
    return {
        'token': jwt_encode_handler(jwt_payload_handler(instance))
    }