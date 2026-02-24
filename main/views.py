from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import JsonResponse
from .models import MessageForMe


class Homepage(CreateView):
    model = MessageForMe
    fields = ["fullname", "phone", "subject", "message"]
    template_name = "index.html"
    success_url = reverse_lazy("Homepage")

    def form_valid(self, form):
        self.object = form.save()  # faqat 1 marta save

        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse(
                {"status": "success", "message": "Xabaringiz yetkazildi!"}
            )

        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse(
                {"status": "error", "message": "Xabaringiz yetkazilmadi!"}
            )

        return super().form_invalid(form)
