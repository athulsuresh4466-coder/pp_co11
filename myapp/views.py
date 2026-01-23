from django.shortcuts import render

# Create your views here.

from .models import (
    Service,
    HomeService,
    ContactMessage,
    AboutSection,
    Project,          # 👈 ADD THIS
)
def page5(request):
    services = Service.objects.all()
    home_services = HomeService.objects.filter(is_active=True)
    about_sections = AboutSection.objects.all()
    projects = Project.objects.all()   # 👈 ADD THIS

    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            service=request.POST.get("service"),
            message=request.POST.get("message"),
        )

    return render(request, "new.html", {
        "services": services,
        "home_services": home_services,
        "about_sections": about_sections,
        "projects": projects,     # 👈 PASS TO TEMPLATE
    })