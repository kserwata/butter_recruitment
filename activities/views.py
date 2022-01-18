from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
import logging
from rest_framework.response import Response
from activities.models import Activity
from activities.serializers import ActivitiesSerializer, AggregateActivitySerializer

logger = logging.getLogger('django')


class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitiesSerializer

    @action(methods=['post'], detail=False, url_path='import')
    def import_data(self, request, *args, **kwargs):
        for data in request.data:
            serializer_data = self.get_serializer(data=data)
            if serializer_data.is_valid():
                self.perform_create(serializer_data)
            else:
                logger.warning('Failed to insert activity, errors: {}'.format(serializer_data.errors))
        return super().list(self, request, *args, **kwargs)

    @action(methods=['get'], detail=False, url_path='aggregate')
    def aggregate_data(self, request, *args, **kwargs):
        if not request.query_params.get('track_id', None):
            raise KeyError('track_id is not present in request')
        activities_by_track_id = Activity.objects.filter(track_id=request.query_params['track_id'])
        if activities_by_track_id.exists():
            settlement = activities_by_track_id.filter(status='S').aggregate(amount=Sum('billing_amount'))
            refunds = activities_by_track_id.filter(status='R').aggregate(amount=Sum('billing_amount'))
            return Response(AggregateActivitySerializer({
                'track_id': request.query_params['track_id'],
                'amount': settlement['amount'] - refunds['amount'],
                'last_status': activities_by_track_id.order_by('activity_date').last().status
            }).data)
        else:
            return Response()
