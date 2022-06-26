from app.api.views.StudentApplications import (
    StudentApplicationsList,
    StudentApplicationsRetrieveUpdateDestroy,
    ApplicationsViewSets,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Viewsets Route
router = DefaultRouter()
router.register('posts', ApplicationsViewSets)

urlpatterns = [
    # Post
    path(
        "",
        StudentApplicationsList.as_view(),
        name="Apllications List",
    ),

    # Get Put Delete
    path(
        "<int:pk>",
        StudentApplicationsRetrieveUpdateDestroy.as_view(),
        name="Applications Delete Update Get",
    ),

    # Viewsets
    path(
    "",
    include(router.urls),
    ),

]