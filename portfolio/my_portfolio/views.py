from django.shortcuts import render ,redirect
from .models import Project
from django.core.mail import send_mail
from django.contrib import messages




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



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(request, "All fields are required!")
            return redirect("contact")  # Redirect to the same page

        # Email details
        subject = f"New Contact Message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_email = "diwashshrestha108@gmail.com"  # Replace with your email

        try:
            send_mail(subject, body, email, [recipient_email])
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send message: {e}")

        return redirect("contact")  # Redirect after processing

    return render(request, "contact.html")
