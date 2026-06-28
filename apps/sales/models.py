# apps/sale/models.py
from django.db import models
from django.conf import settings
from apps.choreography.models import Choreography
import uuid

class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name='sales'
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    class PaymentStatus(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        
    payment_status = models.CharField(
        max_length=20, 
        choices=PaymentStatus.choices, 
        default=PaymentStatus.PENDING
    )
    billing_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta {self.id} - Estado: {self.payment_status}"


class SaleDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale = models.ForeignKey(
        Sale, 
        on_delete=models.CASCADE, 
        related_name='details'
    )
    choreography = models.ForeignKey(
        Choreography, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='sale_details'
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='enrollments'
    )
    choreography = models.ForeignKey(
        Choreography, 
        on_delete=models.CASCADE, 
        related_name='enrollments'
    )
    acquired_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('client', 'choreography')


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='reviews'
    )
    choreography = models.ForeignKey(
        Choreography, 
        on_delete=models.CASCADE, 
        related_name='reviews'
    )
    rating = models.IntegerField()  # Validación de rango 1-5 se manejará en Serializers/Formularios
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('client', 'choreography')


class RatingLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    choreography = models.ForeignKey(Choreography, on_delete=models.CASCADE)
    old_rating = models.IntegerField(null=True, blank=True)
    new_rating = models.IntegerField()
    
    class LogAction(models.TextChoices):
        CREATE = 'create', 'Create'
        UPDATE = 'update', 'Update'
        DELETE = 'delete', 'Delete'
        
    action_type = models.CharField(max_length=20, choices=LogAction.choices)
    registered_at = models.DateTimeField(auto_now_add=True)