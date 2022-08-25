from user.models import User
from billing.models import Invoice, ItemLine
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]


class ItemLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLine
        fields = ["quantity", "description", "price", "taxed"]


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ["user", "date", "due_date", "items"]

    items = ItemLineSerializer(many=True)

    def create(self, validated_data):
        items = validated_data.pop("items")
        invoice = Invoice.objects.create(**validated_data)
        for item in items:
            ItemLine.objects.create(invoice=invoice, **item)
        return invoice
