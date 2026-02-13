from django import forms
from .models import Customer, Measurement, Order


# -----------------------------
# Customer Form
# -----------------------------
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


# -----------------------------
# Measurement Form
# -----------------------------
class MeasurementForm(forms.ModelForm):

    class Meta:
        model = Measurement
        exclude = ['created_at']
        widgets = {

            'customer': forms.Select(attrs={'class': 'form-control'}),
            'dress_type': forms.Select(attrs={'class': 'form-control'}),

            # Upper body
            'shoulder': forms.NumberInput(attrs={'class': 'form-control'}),
            'bust': forms.NumberInput(attrs={'class': 'form-control'}),
            'underbust': forms.NumberInput(attrs={'class': 'form-control'}),
            'waist': forms.NumberInput(attrs={'class': 'form-control'}),
            'hip': forms.NumberInput(attrs={'class': 'form-control'}),
            'armhole': forms.NumberInput(attrs={'class': 'form-control'}),
            'sleeve_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'bicep_round': forms.NumberInput(attrs={'class': 'form-control'}),
            'elbow_round': forms.NumberInput(attrs={'class': 'form-control'}),
            'wrist_round': forms.NumberInput(attrs={'class': 'form-control'}),

            # Special
            'neck_depth_front': forms.NumberInput(attrs={'class': 'form-control'}),
            'neck_depth_back': forms.NumberInput(attrs={'class': 'form-control'}),
            'blouse_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'kurti_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'suit_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'full_length': forms.NumberInput(attrs={'class': 'form-control'}),
            'apex': forms.NumberInput(attrs={'class': 'form-control'}),
            'shoulder_to_apex': forms.NumberInput(attrs={'class': 'form-control'}),
            'slit_length': forms.NumberInput(attrs={'class': 'form-control'}),

            # Lower body
            'thigh': forms.NumberInput(attrs={'class': 'form-control'}),
            'knee': forms.NumberInput(attrs={'class': 'form-control'}),
            'calf': forms.NumberInput(attrs={'class': 'form-control'}),
            'bottom_round': forms.NumberInput(attrs={'class': 'form-control'}),
            'ankle': forms.NumberInput(attrs={'class': 'form-control'}),
            'flare': forms.NumberInput(attrs={'class': 'form-control'}),
            'cancan_length': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# -----------------------------
# Order Form
# -----------------------------
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'dress_type', 'delivery_date', 'price', 'status']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'dress_type': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
