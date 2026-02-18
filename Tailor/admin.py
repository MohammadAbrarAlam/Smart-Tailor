from django.contrib import admin
from .models import Customer, Measurement, Order

# Customer Admin 
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "created_at")
    search_fields = ("name", "phone")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    auto_now_add=True


# ==============================
# Measurement Admin
# ==============================
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):

    list_display = (
        "customer",
        "dress_type",
        "created_at"
    )

    list_filter = (
        "dress_type",
        "created_at",
    )

    search_fields = (
        "customer__name",
        "dress_type",
    )

    ordering = ("-created_at",)

    fieldsets = (

        ("Basic Information", {
            "fields": ("customer", "dress_type")
        }),

        ("Upper Body Measurements", {
            "fields": (
                "shoulder", "bust", "underbust",
                "waist", "hip", "armhole",
                "sleeve_length", "bicep_round",
                "elbow_round", "wrist_round"
            ),
            "classes": ("collapse",)
        }),

        ("Neck & Special Measurements", {
            "fields": (
                "neck_depth_front", "neck_depth_back",
                "apex", "shoulder_to_apex",
                "slit_length"
            ),
            "classes": ("collapse",)
        }),

        ("Dress Specific Lengths", {
            "fields": (
                "blouse_length",
                "kurti_length",
                "suit_length",
                "full_length"
            ),
            "classes": ("collapse",)
        }),

        ("Lower Body Measurements", {
            "fields": (
                "thigh", "knee", "calf",
                "bottom_round", "ankle",
                "flare", "cancan_length"
            ),
            "classes": ("collapse",)
        }),

        ("Metadata", {
            "fields": ("created_at",)
        }),
    )

    readonly_fields = ("created_at",)


# ==============================
# Order Admin
# ==============================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "customer",
        "dress_type",
        "coming_date",
        "delivery_date",
        "price",
        "status",
    )

    list_filter = (
        "status",
        "dress_type",
        "coming_date",
        "delivery_date",
    )

    search_fields = (
        "customer__name",
        "dress_type",
    )

    ordering = ("-coming_date",)
    readonly_fields = ("coming_date",)
