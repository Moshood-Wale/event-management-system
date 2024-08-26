from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    event = models.ForeignKey(Event, related_name='tickets', on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    sold = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.ticket_type} for {self.event.name}"

    def buy_ticket(self, quantity):
        if self.sold + quantity > self.quantity:
            raise ValueError("Not enough tickets available")
        self.sold += quantity
        self.save()
    

    
