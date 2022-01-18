from rest_framework import serializers

from activities.models import Activity


class ActivitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ['id', 'track_id', 'activity_date', 'track_id', 'status', 'billing_amount']


class AggregateActivitySerializer(serializers.Serializer):
    track_id = serializers.CharField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    last_status = serializers.CharField()
