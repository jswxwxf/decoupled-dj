# Generated by Django 4.1 on 2022-08-25 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('taxed', models.BooleanField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='billing.invoice')),
            ],
        ),
        migrations.DeleteModel(
            name='LineItem',
        ),
    ]
