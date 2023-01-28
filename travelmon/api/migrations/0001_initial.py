# Generated by Django 4.1.5 on 2023-01-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("email", models.EmailField(max_length=60, unique=True)),
                ("username", models.CharField(max_length=30, unique=True)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("last_login", models.DateTimeField(auto_now=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("user_score", models.PositiveIntegerField(default=0)),
                (
                    "duel_code",
                    models.CharField(blank=True, default="", max_length=6, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
