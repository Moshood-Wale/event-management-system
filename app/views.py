from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Ticket, Event
from .serializers import EventSerializer, TicketSerializer, BuyTicketSerializer


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class BuyTicketView(generics.GenericAPIView):
    queryset = Ticket.objects.all()
    serializer_class = BuyTicketSerializer

    def post(self, request, *args, **kwargs):
        ticket = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quantity = serializer.validated_data['quantity']

        try:
            ticket.buy_ticket(quantity)
        except ValueError as e:
            raise ValidationError(str(e))
        
        return Response({'message': 'Ticket purchased successfully!'}, status=status.HTTP_200_OK)
