# Generated by Django 3.0.10 on 2020-10-10 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s_inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(blank=True, max_length=16, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('OK', 'Complete'), ('SA', 'Set Aside'), ('NW', 'New')], default='NW', max_length=2)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('amount_received', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('change', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='s_core.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('item_stock', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='s_inventory.ItemStock')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='s_core.Purchase')),
                ('quantity_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='s_inventory.QuantityUnit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
