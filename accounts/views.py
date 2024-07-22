from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup_page.html"
    context_object_name = "form"

    def get_success_url(self):
        return reverse("login")

# def signup_view(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "registration/signup_page.html", context={"form": form})
