# Generated by Django 3.1.1 on 2020-09-22 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('brand', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('vendor', models.CharField(max_length=64)),
                ('num_cartridges', models.IntegerField(default=0)),
                ('cart_on_hand', models.IntegerField(default=0)),
                ('product_url', models.URLField()),
            ],
        ),
    ]