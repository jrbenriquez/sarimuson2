# Generated by Django 3.0.10 on 2020-10-17 15:55

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='s_inventory.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='s_inventory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ItemStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=32, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('price_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('active', models.BooleanField(default=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='s_inventory.Item')),
            ],
        ),
        migrations.CreateModel(
            name='QuantityUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('short_name', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuantityUnitPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=11)),
                ('quantity_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='s_inventory.QuantityUnit')),
                ('stock', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='s_inventory.ItemStock')),
            ],
        ),
        migrations.AddField(
            model_name='itemstock',
            name='quantity_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='s_inventory.QuantityUnit'),
        ),
    ]
