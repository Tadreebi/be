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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic.base import RedirectView

from app.api.views import logout_view

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("company-ratings/", include("app.urls.CompanyRating")),
    path("company-reports/", include("app.urls.CompanyReport")),
    path("opportunity-posts/", include("app.urls.InternshipPost")),
    path("opportunity-applications/", include("app.urls.StudentApplication")),
    path("students/experiences/", include("app.urls.StudentExperience")),
    path("students/goals/", include("app.urls.StudentGoal")),
    path("students/profile/", include("app.urls.StudentProfile")),
    path("students/proposals/", include("app.urls.StudentProposal")),
    path("university/proposals-response/", include("app.urls.UniProposalResponse")),
    path(
        "company/application-response/", include("app.urls.StudentApplicationResponse")
    ),
    path("students/reports/", include("app.urls.StudentReport")),
    path("univeristy-feedbacks/", include("app.urls.UniversityFeedback")),
    path("faculty-major/", include("app.urls.Faculty")),
    path("supervised-by/", include("app.urls.SupervisedBy")),
    path("univeristy-tips/", include("app.urls.UniversityTip")),
    path("cities/", include("app.urls.Cities")),  # no need for it
    path("accounts/", include("django.contrib.auth.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/logout/", logout_view, name="logout"),  # dont use it
    path("token/", include("app.urls.Token")),
    path("", include("app.urls.User")),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("", RedirectView.as_view(url="/swagger/", permanent=True)),
]
# Students Resumes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
