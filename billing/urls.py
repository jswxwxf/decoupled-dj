from django.urls import path

from .api.views import ClientList, InvoiceCreate
from .views import Index

app_name = "billing"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("api/clients/", ClientList.as_view(), name="client-list"),
    path('api/invoices/', InvoiceCreate.as_view(), name="invoice-create")
]
