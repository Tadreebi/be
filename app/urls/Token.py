from django.urls import path
from app.api.views import TokenView

urlpatterns = [
    path("", TokenView.as_view(), name="token"),
]
