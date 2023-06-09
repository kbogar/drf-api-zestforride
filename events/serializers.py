from rest_framework import serializers
from .models import Event
from interested.models import Interested


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for Event model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    interested_id = serializers.SerializerMethodField()
    interested_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        It checks for image size limit of 2MB.
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_interested_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            interested = Interested.objects.filter(
                owner=user, event=obj
            ).first()
            return interested.id if interested else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'event_details', 'date', 'time', 'is_owner', 'image', 'profile_id',
            'profile_image', 'interested_id', 'interested_count',
        ]
