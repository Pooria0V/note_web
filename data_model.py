from django.apps import apps
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



import os
import django

# تنظیم مسیر به فایل settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'note_web.settings')

# مقداردهی اولیه جنگو
django.setup()

def get_models_info():
    models_info = []
    for model in apps.get_models():
        fields = [field.name for field in model._meta.fields]
        models_info.append({
            'model_name': model.__name__,
            'fields': fields,
        })
    return models_info


def create_pdf(models_info, filename='models.pdf'):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750  # موقعیت اولیه برای متن

    for model in models_info:
        c.drawString(50, y, f"Model: {model['model_name']}")
        y -= 20
        for field in model['fields']:
            c.drawString(70, y, f"- {field}")
            y -= 15
        y -= 30  # فاصله بین مدل‌ها

        if y < 50:  # اگر به انتهای صفحه رسیدیم
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750

    c.save()

models_info = get_models_info()

create_pdf(models_info)

# from django.apps import apps
# from weasyprint import HTML
#
# def generate_html(models_info):
#     html_content = "<h1>Data Models</h1>"
#     for model in models_info:
#         html_content += f"<h2>{model['model_name']}</h2><ul>"
#         for field in model['fields']:
#             html_content += f"<li>{field}</li>"
#         html_content += "</ul>"
#     return html_content
#
# def create_pdf(models_info, filename='models.pdf'):
#     html_content = generate_html(models_info)
#     HTML(string=html_content).write_pdf(filename)
#
# models_info = get_models_info()
# create_pdf(models_info)
