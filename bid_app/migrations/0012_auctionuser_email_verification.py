# Generated by Django 4.0.4 on 2022-05-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid_app', '0011_auctionuser_account_number_auctionuser_adhar_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionuser',
            name='email_verification',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
