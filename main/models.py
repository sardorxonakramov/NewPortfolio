from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class MessageForMe(models.Model):
    fullname = models.CharField(max_length=40, verbose_name="Full Name")
    phone = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r"^\+998\d{9}$",
                message="Telefon raqam formati: +998901234567 bo'lishi kerak.",
            )
        ],
        help_text="Masalan: +998901234567",
    )
    subject = models.CharField(
        max_length=50,
        verbose_name="Mavzu",
        null=True,
        blank=True,
    )

    message = models.TextField(verbose_name="Xabar matni: ")
