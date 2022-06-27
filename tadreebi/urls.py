"""tadreebi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("students/", include("app.urls.studentReports")),
    path("proposal/", include("app.urls.StudentProposal")),
    path("profile/", include("app.urls.studentProfile")),
    path("post/", include("app.urls.internshipPost")),
    path("apply/", include("app.urls.studentApplications")),
    path("companyReport/", include("app.urls.CompanyReport")),
    path("comapnyRating/", include("app.urls.ComapnyRating")),
    path("experience/", include("app.urls.studentExperience")),
    path("comp-uni-feedback/", include("app.urls.comp_uni_urls")),
    path("uni-stu-feedback/", include("app.urls.uni_stu_urls")),
    path("/", include("app.urls.Users")),
]
# Students Resumes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
