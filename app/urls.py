from django.urls import path
from .views import EventListCreateView, TicketListCreateView, TicketDetailView, BuyTicketView


urlpatterns = [
    path('events/', EventListCreateView.as_view(), name= 'event-list-create'),
    path('tickets/', TicketListCreateView.as_view(), name= 'ticket-list-create'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name= 'ticket-detail'),
    path('tickets/<int:pk>/buy/', BuyTicketView.as_view(), name= 'buy-ticket'),
]
