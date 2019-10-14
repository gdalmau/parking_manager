from django.urls import path
from parking_app import views

app_name = 'parking_app'

urlpatterns = [
    path('reservations/', views.ReservationCreateAPIView.as_view(), name="reservation-create"),
    path('reservations', views.ReservationListAPIView.as_view(), name="reservation-list"),
]
