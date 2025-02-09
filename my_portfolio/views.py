from django.shortcuts import render, redirect
from .models import Project
from django.core.mail import send_mail
from django.contrib import messages
from django import forms
from django.conf import settings



def homepage(request):
    projects = Project.objects.all()
    return render(request, 'home.html',{'projects':projects})
    

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html',{'projects':projects})

def resume(request):
    return render(request, 'resume.html')

# Contact Form using Django Forms (adds validation)
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,  # Secure email settings
                    ["your_email@gmail.com"],  # Receiver email
                    fail_silently=False,
                )
                messages.success(request, "Message sent successfully!")
                return redirect("contact")  # Redirect only after successful submission
            except Exception as e:
                messages.error(request, f"Error sending message: {e}")
        else:
            messages.error(request, "Please fill in all fields correctly.")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
