from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Customer, Measurement, Order
from .forms import CustomerForm, MeasurementForm, OrderForm
from .utils import generate_customer_qr, export_to_excel


# ==============================
# Dashboard
# ==============================
def dashboard(request):
    context = {
        "total_customers": Customer.objects.count(),
        "total_orders": Order.objects.count(),
        "pending_orders": Order.objects.filter(status="Pending").count(),
        "completed_orders": Order.objects.filter(status="Completed").count(),
    }
    return render(request, "Tailor/dashboard.html", context)


# ==============================
# Add Customer + QR (Using utils)
# ==============================
def add_customer(request):
    form = CustomerForm(request.POST or None)

    if form.is_valid():
        customer = form.save()

        # 🔥 Generate QR using utils
        generate_customer_qr(customer)

        messages.success(request, "Customer added & QR generated successfully!")
        return redirect("customer_list")

    return render(request, "Tailor/add_customer.html", {"form": form})


# ==============================
# Customer List
# ==============================
def customer_list(request):
    customers = Customer.objects.all().order_by("-created_at")
    return render(request, "Tailor/customer_list.html", {"customers": customers})


# ==============================
# Customer Detail
# ==============================
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    context = {
        "customer": customer,
        "measurements":customer.measurements.all(),
        "orders": customer.orders.all(),
    }

    return render(request, "Tailor/customer_detail.html", context)


# ==============================
# Add Measurement
# ==============================
def add_measurement(request, customer_id=None):

    # 🔹 If coming from customer detail page
    if customer_id:
        customer = get_object_or_404(Customer, id=customer_id)
    else:
        customer = None

    if request.method == "POST":
        form = MeasurementForm(request.POST)

        if form.is_valid():
            measurement = form.save(commit=False)

            # 🔥 If customer_id passed in URL
            if customer:
                measurement.customer = customer

            measurement.save()

            messages.success(
                request,
                f"{measurement.dress_type} measurement added successfully!"
            )

            return redirect("customer_detail", pk=measurement.customer.id)

    else:
        form = MeasurementForm(initial={"customer": customer} if customer else None)

    return render(request, "Tailor/add_measurement.html", {
        "form": form,
        "customer": customer
    })


# ==============================
# Add Order
# ==============================
def add_order(request):
    form = OrderForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Order created successfully!")
        return redirect("customer_list")

    return render(request, "Tailor/add_order.html", {"form": form})


# ==============================
# Update Order
# ==============================
def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)

    if form.is_valid():
        form.save()
        messages.success(request, "Order updated successfully!")
        return redirect("customer_detail", pk=order.customer.id)

    return render(request, "Tailor/update_order.html", {"form": form})


# ==============================
# Delete Customer
# ==============================
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        customer.delete()
        messages.success(request, "Customer deleted successfully!")
        return redirect("customer_list")

    return render(request, "Tailor/delete_customer.html", {"customer": customer})


# ==============================
# Export Customers (Using utils)
# ==============================
def export_customers_excel(request):
    customers = Customer.objects.all().values(
        "name",
        "phone",
        "created_at"
    )
    columns = ["Name", "Phone", "Created At"]

    return export_to_excel(customers, columns, "customers.xlsx")

# ==============================
# Export Orders (Using utils)
# ==============================
def export_orders_excel(request):

    orders = Order.objects.all().values(
        "customer__name",
        "dress_type",
        "coming_date",
        "delivery_date",
        "price",
        "status"
    )

    columns = [
        "Customer Name",
        "Dress Type",
        "Order Date",
        "Delivery Date",
        "Price",
        "Status"
    ]

    return export_to_excel(orders, columns, "orders.xlsx")
