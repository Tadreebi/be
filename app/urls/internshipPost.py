from app.api.views.InternshipPost import (
    PostInternshipList,
    PostInternshipRetrieveUpdateDestroy,
    PostsViewSets,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api.views import FilterPosts
# Viewsets Route
router = DefaultRouter()
router.register('posts', PostsViewSets)

urlpatterns = [
    # Post
    path(
        "",
        PostInternshipList.as_view(),
        name="Internship Posts List",
    ),

    # Get Put Delete
    path(
        "<int:pk>",
        PostInternshipRetrieveUpdateDestroy.as_view(),
        name="Internship Posts Delete Update Get",
    ),

    # Viewsets
    path(
    "",
    include(router.urls),
    ),
]