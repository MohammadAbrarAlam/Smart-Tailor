import os
import qrcode
import pandas as pd
from django.conf import settings
from django.http import HttpResponse
from datetime import date


# =====================================
# Create Folder If Not Exists
# =====================================
def create_folder(folder_name):
    folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


# =====================================
# Generate QR Code for Customer
# =====================================
def generate_customer_qr(customer):
    qr_folder = create_folder("qr_codes")

    qr_data = str(customer.name)

    qr_img = qrcode.make(qr_data)

    qr_path = os.path.join(qr_folder, f"{customer.name}.png")
    qr_img.save(qr_path)

    return qr_path


# =====================================
# Export Data to Excel
# =====================================

def export_to_excel(queryset, columns, filename):

    df = pd.DataFrame(list(queryset))

    if df.empty:
        df = pd.DataFrame(columns=columns)
    else:
        df.columns = columns

        # 🔥 Force convert datetime safely
        for col in df.select_dtypes(include=['datetimetz']).columns:
            df[col] = df[col].dt.tz_localize(None)

    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    df.to_excel(file_path, index=False)

    response = HttpResponse(
        open(file_path, 'rb'),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response

# =====================================
# Check Overdue Orders
# =====================================
def get_overdue_orders(OrderModel):
    today = date.today()
    return OrderModel.objects.filter(delivery_date__lt=today, status="Pending")
