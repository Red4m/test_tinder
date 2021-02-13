# Generated by Django 3.1.6 on 2021-02-12 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0001_initial'),
        ('profile', '0005_auto_20210204_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='type_of_subscriber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_of_subscriber', to='subscriber.subscriber'),
        ),
    ]