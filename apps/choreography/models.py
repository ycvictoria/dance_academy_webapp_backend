# apps/choreography/models.py
from django.db import models
from django.conf import settings
import uuid

class DanceStyle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Choreography(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    class Difficulty(models.TextChoices):
        BASIC = 'basic', 'Basic'
        INTERMEDIATE = 'intermediate', 'Intermediate'
        ADVANCED = 'advanced', 'Advanced'
        
    difficulty_level = models.CharField(max_length=20, choices=Difficulty.choices)
    thumbnail_url = models.URLField(max_length=255)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Relaciones nativas de Django hacia el modelo User y DanceStyle
    main_teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name='main_choreographies'
    )
    dance_style = models.ForeignKey(
        DanceStyle, 
        on_delete=models.PROTECT, 
        related_name='choreographies'
    )
    guest_teachers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='guest_choreographies',
        blank=True
    )

    def __str__(self):
        return self.title


class VideoClip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    choreography = models.ForeignKey(
        Choreography, 
        on_delete=models.CASCADE, 
        related_name='videos'
    )
    title = models.CharField(max_length=150)
    video_url = models.URLField(max_length=255)
    sequence_order = models.IntegerField()
    duration_seconds = models.IntegerField()

    class Meta:
        ordering = ['sequence_order']

    def __str__(self):
        return f"{self.choreography.title} - {self.title}"


class ChoreographyStat(models.Model):
    # Relación uno a uno que sirve como llave primaria (Tabla Satélite)
    choreography = models.OneToOneField(
        Choreography, 
        on_delete=models.CASCADE, 
        primary_key=True, 
        related_name='stats'
    )
    actual_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_views = models.IntegerField(default=0)
    total_sales_count = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)


class VideoPlaybackLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video_clip = models.ForeignKey(VideoClip, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class PriceLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    choreography = models.ForeignKey(Choreography, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    registered_at = models.DateTimeField(auto_now_add=True)