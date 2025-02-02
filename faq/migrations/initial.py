import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FAQ",
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
                ("question", models.TextField()),
                ("answer", ckeditor.fields.RichTextField()),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English"), ("hi", "Hindi"), ("bn", "Bengali")],
                        default="en",
                        max_length=2,
                    ),
                ),
                ("question_hi", models.TextField(blank=True, null=True)),
                ("question_bn", models.TextField(blank=True, null=True)),
                ("answer_hi", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("answer_bn", ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]