# 🧵 SmartTailor

SmartTailor is a Django-based tailoring management system that helps tailoring shops manage customers, measurements, and orders digitally.

It replaces manual record-keeping with a structured, scalable web solution.

---

## 🚀 Features

- 👤 Customer Management
- 📏 Dress-Type Based Measurement System
- 🧾 Order Tracking System
- 📊 Excel Export (Customers & Orders)
- 🔐 Django Admin Panel
- 🖥 Dashboard Analytics
- ⚡ Dynamic Measurement Form (Auto field show/hide)
- 🆔 UUID-based Customer ID

---

## 🏗 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Excel Export:** Pandas + OpenPyXL
- **QR Code:** qrcode + Pillow
- **Deployment:** Render

---

## 📂 Project Structure

```
SmartTailor/
│
├── Tailor/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   └── utils.py
│
├── templates/
│   └── Tailor/
│       ├── base.html
│       ├── dashboard.html
│       ├── add_customer.html
│       ├── add_measurement.html
│       ├── customer_detail.html
│
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🧵 Dress Type Measurement System

Supported Dress Types:

- Blouse
- Kurti
- Suit
- Salwar
- Lehenga
- Gown

Each dress type dynamically displays only relevant measurement fields.

Example (Blouse):

- Bust
- Waist
- Sleeve Length
- Neck Depth (Front/Back)
- Apex
- Shoulder to Apex

---

# ⚙️ Installation (Without Virtual Environment)

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/SmartTailor.git
cd SmartTailor
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Run Migrations

```bash
python manage.py migrate
```

## 4️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

## 5️⃣ Run Server

```bash
python manage.py runserver
```

Open:
```
http://127.0.0.1:8000
```

---

# 📊 Excel Export

You can export:

- Customers → `/export/customers/`
- Orders → `/export/orders/`

Files are generated in:

```
media/
```

---

# 🔐 Admin Panel

Access:
```
/admin
```

Admin can:

- Add/Edit Customers
- Manage Measurements
- Track Orders
- Filter by Dress Type
- Search by Customer Name

---

# 🌍 Deployment on Render

## Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial Commit - SmartTailor"
git branch -M main
git remote add origin https://github.com/your-username/SmartTailor.git
git push -u origin main
```

---

## Step 2: requirements.txt

Make sure it includes:

```
Django==5.2.8
gunicorn
pandas
openpyxl
qrcode
Pillow
psycopg2-binary
```

---

## Step 3: Create Procfile

Create file:

```
Procfile
```

Add:

```
web: gunicorn SmartTailor.wsgi
```

---

## Step 4: Update settings.py for Production

```python
import os

DEBUG = False
ALLOWED_HOSTS = ['.onrender.com']

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```

---

## Step 5: Deploy on Render

1. Go to https://render.com
2. New Web Service
3. Connect GitHub repo
4. Build Command:

```
pip install -r requirements.txt
```

5. Start Command:

```
gunicorn SmartTailor.wsgi
```

Deploy 🚀

---

# 🔮 Future Enhancements

- 📄 PDF Invoice Generation
- 📩 SMS Notifications
- 📱 Mobile Responsive UI
- 🧾 Billing System
- 📈 Profit Analytics Dashboard
- 🧵 Fabric Stock Management
- 👥 Staff Role Management

---

# 👨‍💻 Author

**Abrar Alam**  
Python & Django Developer  

---

# 📜 License

This project is licensed under the MIT License.
