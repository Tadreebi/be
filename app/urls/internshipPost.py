from app.api.views import (
    InternshipPostList,
    InternshipPostRetrieveUpdateDestroy,
    InternshipPostsViewSets,
    InternshipPostRequirementsList,
    InternshipPostRequirementsRetrieveUpdateDestroy,
    InternshipPostRequirementsViewSets,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Viewsets Route
router = DefaultRouter()
router.register("posts", InternshipPostsViewSets)
router.register("requirements", InternshipPostRequirementsViewSets)


urlpatterns = [
    # Post
    path(
        "",
        InternshipPostList.as_view(),
        name="Internship Posts List",
    ),
    # Get Put Delete
    path(
        "<int:pk>",
        InternshipPostRetrieveUpdateDestroy.as_view(),
        name="Internship Posts Delete Update Get",
    ),
    # Viewsets
    path(
        "",
        include(router.urls),
    ),
    # Post
    path(
        "requirements/",
        InternshipPostRequirementsList.as_view(),
        name="Internship Posts List",
    ),
    # Get Put Delete
    path(
        "requirements/<int:pk>",
        InternshipPostRequirementsRetrieveUpdateDestroy.as_view(),
        name="Internship Posts Delete Update Get",
    ),
    # Viewsets
    path(
        "requirements",
        include(router.urls),
    ),
]
