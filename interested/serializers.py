from rest_framework import serializers
from .models import Interested
from django.db import IntegrityError


class InterestedSerializer(serializers.ModelSerializer):
    """
    Interested Serializer.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Interested
        fields = [
            'id', 'owner', 'event', 'created_at',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
