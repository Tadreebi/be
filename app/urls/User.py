from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from app.api.views import (
    StudentSignUpView,
    UniversitySignUpView,
    CompanySignUpView,
    StudentSignUpDetail,
    UniversitySignUpDetail,
    CompanySignUpDetail,
    StudentUserListView,
    UniversityEmployeeUserListView,
    CompanyUserListView,
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
        "accounts/student/<str:username>/",
        StudentSignUpDetail.as_view(),
        name="student_detail",
    ),
    path(
        "accounts/university/<str:username>/",
        UniversitySignUpDetail.as_view(),
        name="university_detail",
    ),
    path(
        "accounts/company/<str:username>/",
        CompanySignUpDetail.as_view(),
        name="company_detail",
    ),
    path("accounts/student-list", StudentUserListView.as_view(), name="student_list"),
    path("accounts/university-list", UniversityEmployeeUserListView.as_view(), name="university_list"),
    path("accounts/company-list", CompanyUserListView.as_view(), name="company_list"),
]
