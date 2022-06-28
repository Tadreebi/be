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
    path("comapny-ratings/", include("app.urls.ComapnyRating")),
    path("comapny-feedbacks/", include("app.urls.comp_uni_urls")),
    path("company-reports/", include("app.urls.CompanyReport")),
    path("opportunity-posts/", include("app.urls.internshipPost")),
    path("opportunity-applications/", include("app.urls.studentApplications")),
    path("students/experiences/", include("app.urls.studentExperience")),
    path("students/goals/", include("app.urls.studentGoals")),
    path("students/profile/", include("app.urls.studentProfile")),
    path("students/proposals/", include("app.urls.StudentProposal")),
    path("students/", include("app.urls.studentReports")),
    path("univeristy-feedbacks/", include("app.urls.uni_stu_urls")),
    path("univeristy-tips/", include("app.urls.universityTips")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("/", include("app.urls.Users")),
]
# Students Resumes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
