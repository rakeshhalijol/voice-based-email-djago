# Generated by Django 4.0.1 on 2022-04-20 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciver', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
