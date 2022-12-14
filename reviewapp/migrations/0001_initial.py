# Generated by Django 4.1.1 on 2022-09-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tags",
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
                ("tag_name", models.CharField(max_length=10)),
            ],
            options={"ordering": ["tag_name"],},
        ),
        migrations.CreateModel(
            name="companyReview",
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
                ("company_name", models.CharField(max_length=15)),
                ("review", models.TextField()),
                ("worked_here", models.BooleanField(default=True)),
                ("date_posted", models.DateField(auto_now_add=True)),
                ("tags", models.ManyToManyField(to="reviewapp.tags")),
            ],
            options={"ordering": ["-date_posted"],},
        ),
    ]
