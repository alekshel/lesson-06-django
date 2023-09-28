# Generated by Django 4.2.5 on 2023-09-28 09:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                (
                    "first_name",
                    models.CharField(default="", max_length=255, verbose_name="Ім'я"),
                ),
                (
                    "last_name",
                    models.CharField(
                        default="", max_length=255, verbose_name="Прізвище"
                    ),
                ),
                ("subject", models.DateField(default="", verbose_name="Предмет")),
            ],
            options={
                "verbose_name": "Вчитель",
                "verbose_name_plural": "Вчителі",
            },
        ),
    ]
