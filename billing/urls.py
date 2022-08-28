from ariadne_django.views import GraphQLView
from django.urls import path

from .api.views import ClientList, InvoiceCreate
from .views import Index
from .schema import schema

app_name = "billing"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("api/clients/", ClientList.as_view(), name="client-list"),
    path('api/invoices/', InvoiceCreate.as_view(), name="invoice-create"),
    path("graphql/", GraphQLView.as_view(schema=schema), name="graphql")
]
