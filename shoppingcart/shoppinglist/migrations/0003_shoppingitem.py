# Generated by Django 4.2.7 on 2023-11-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0002_customuser_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('note', models.CharField(max_length=50)),
            ],
        ),
    ]