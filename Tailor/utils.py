import os
import re
import qrcode
import pandas as pd
from django.conf import settings
from django.http import HttpResponse
from datetime import date

# =====================================
# Create Folder If Not Exists
# =====================================
def create_folder(folder_name):
    """
    Create folder under MEDIA_ROOT if it doesn't exist.
    Returns the absolute folder path.
    """
    folder_path = os.path.normpath(os.path.join(settings.MEDIA_ROOT, folder_name))
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


# =====================================
# Generate QR Code for Customer
# =====================================
def generate_customer_qr(customer):
    """
    Generate a QR code for a customer and save it under MEDIA_ROOT/qr_codes.
    Returns the file path of the QR image.
    """
    qr_folder = create_folder("qr_codes")

    # Sanitize filename to remove invalid characters
    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', customer.name)
    qr_filename = f"{safe_name}_{customer.id}.png"
    qr_path = os.path.join(qr_folder, qr_filename)

    # Generate QR code
    qr_data = str(customer.name)
    qr_img = qrcode.make(qr_data)
    qr_img.save(qr_path)

    return qr_path


# =====================================
# Export Data to Excel
# =====================================
def export_to_excel(queryset, columns, filename):
    """
    Export a queryset or list of dicts to Excel and return as HTTP response.
    - queryset: list of dicts or Django queryset
    - columns: list of column names for Excel
    - filename: name of the Excel file to create
    """
    # Convert queryset to list of dicts if necessary
    df = pd.DataFrame(list(queryset))

    # Ensure dataframe has correct columns
    if df.empty:
        df = pd.DataFrame(columns=columns)
    else:
        if len(columns) == len(df.columns):
            df.columns = columns
        # Handle datetime columns safely
        for col in df.select_dtypes(include=['datetime64[ns, tz]']).columns:
            df[col] = df[col].dt.tz_localize(None)

    # Ensure MEDIA_ROOT exists
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

    # Save Excel file
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    df.to_excel(file_path, index=False)

    # Return as HTTP response safely
    with open(file_path, 'rb') as f:
        response = HttpResponse(
            f.read(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


# =====================================
# Check Overdue Orders
# =====================================
def get_overdue_orders(OrderModel):
    """
    Return queryset of orders that are overdue (delivery_date < today) and pending.
    """
    today = date.today()
    return OrderModel.objects.filter(delivery_date__lt=today, status="Pending")
