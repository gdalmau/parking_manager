from parking_app.models import Customer, Spot, Reservation
from parking_app import serializers


from rest_framework import views, viewsets, generics, status
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime


def create_success(self, data):
    serializer = self.get_serializer(data=data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)

    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED,
                    headers=headers)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

    def create(self, request, *args, **kwargs):
        return create_success(self, request.data)


class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = serializers.SpotSerializer


class ReservationListAPIView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer


class ReservationCreateAPIView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer

    def post(self, request):
        spots = Spot.objects.all()

        customer = Customer.objects.filter(id=request.data['customer']).first()
        if not customer:
            return Response(
                data={'message': 'The customer does not exist'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        datetime_format = '%Y-%m-%d %H:%M'
        start_datetime = datetime.strptime(
            request.data['start_datetime'], datetime_format)
        end_datetime = datetime.strptime(
            request.data['end_datetime'], datetime_format)
        date_range = (start_datetime, end_datetime)
        for spot in spots:
            number = spot.number
            # Find reservations which start or end reservation is between
            # specified dates
            exists_reservation = Reservation.objects.filter(
                Q(spot=spot, start_datetime__range=date_range) |
                Q(spot=spot, end_datetime__range=date_range)
            ).exists()
            if not exists_reservation:
                data = request.data.copy()
                data['spot'] = spot.id
                return create_success(self, data)
        return Response(
            data={'message': 'There are no available spots between the specified times'},
            status=status.HTTP_400_BAD_REQUEST,
        )
