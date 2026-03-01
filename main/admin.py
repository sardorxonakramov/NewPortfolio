from django.contrib import admin
from .models import MessageForMe


@admin.register(MessageForMe)
class MessageForMeAdmin(admin.ModelAdmin):
    list_display = ("fullname", "phone", "subject", "created")
    list_filter = ("created",)
    search_fields = ("fullname", "phone", "subject", "message")
    ordering = ("-created",)
    readonly_fields = ("created",)

    fieldsets = (
        ("Foydalanuvchi ma'lumotlari", {
            "fields": ("fullname", "phone")
        }),
        ("Xabar", {
            "fields": ("subject", "message")
        }),
        ("Vaqt", {
            "fields": ("created",)
        }),
    )