from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import (
    StudentSignUpView,
    UniversitySignUpView,
    CompanySignUpView,
    StudentSignUpDetail,
    UniversitySignUpDetail,
    CompanySignUpDetail,
)


urlpatterns = [
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("accounts/signup/student", StudentSignUpView.as_view(), name="student_signup"),
    path(
        "accounts/signup/university",
        UniversitySignUpView.as_view(),
        name="usinversity_signup",
    ),
    path("accounts/signup/company", CompanySignUpView.as_view(), name="company_signup"),
    path(
        "accounts/student/<int:pk>/",
        StudentSignUpDetail.as_view(),
        name="student_detail",
    ),
    path(
        "accounts/university/<int:pk>/",
        UniversitySignUpDetail.as_view(),
        name="university_detail",
    ),
    path(
        "accounts/company/<int:pk>/",
        CompanySignUpDetail.as_view(),
        name="company_detail",
    ),
]
