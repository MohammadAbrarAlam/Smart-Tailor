from django.db import models
import uuid

class Customer(models.Model):
    customer_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
  
    DRESS_TYPES = [
        ('Blouse', 'Blouse'),
        ('Kurti', 'Kurti'),
        ('Suit', 'Suit'),
        ('Salwar', 'Salwar'),
        ('Lehenga', 'Lehenga'),
        ('Gown', 'Gown'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="measurements"
    )

    dress_type = models.CharField(max_length=50, choices=DRESS_TYPES)

    # Common Upper Measurements
    shoulder = models.FloatField(null=True, blank=True)
    bust = models.FloatField(null=True, blank=True)
    underbust = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    hip = models.FloatField(null=True, blank=True)
    armhole = models.FloatField(null=True, blank=True)
    sleeve_length = models.FloatField(null=True, blank=True)
    bicep_round = models.FloatField(null=True, blank=True)
    elbow_round = models.FloatField(null=True, blank=True)
    wrist_round = models.FloatField(null=True, blank=True)

    # Special Fields
    neck_depth_front = models.FloatField(null=True, blank=True)
    neck_depth_back = models.FloatField(null=True, blank=True)
    blouse_length = models.FloatField(null=True, blank=True)
    kurti_length = models.FloatField(null=True, blank=True)
    suit_length = models.FloatField(null=True, blank=True)
    full_length = models.FloatField(null=True, blank=True)
    apex = models.FloatField(null=True, blank=True)
    shoulder_to_apex = models.FloatField(null=True, blank=True)
    slit_length = models.FloatField(null=True, blank=True)

    # Lower Measurements
    thigh = models.FloatField(null=True, blank=True)
    knee = models.FloatField(null=True, blank=True)
    calf = models.FloatField(null=True, blank=True)
    bottom_round = models.FloatField(null=True, blank=True)
    ankle = models.FloatField(null=True, blank=True)
    flare = models.FloatField(null=True, blank=True)
    cancan_length = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.dress_type}"


class Order(models.Model):
  
    STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    dress_type = models.CharField(max_length=50)

    coming_date = models.DateField(auto_now_add=True)  # 🔥 Auto order date
    delivery_date = models.DateField()

    price = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')

    def __str__(self):
        return f"{self.customer.name} - {self.status}"
