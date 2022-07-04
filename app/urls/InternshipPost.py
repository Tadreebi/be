from app.api.views import (
    InternshipPostList,
    InternshipPostCreate,
    InternshipPostDetail,
    InternshipPostUpdate,
    InternshipPostDelete,
    InternshipPostsViewSets
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Viewsets Route
router = DefaultRouter()
router.register("posts", InternshipPostsViewSets)


urlpatterns = [
    path(
        "posts/",
        InternshipPostList.as_view(),
        name="Student Posts List",
    ),
    path(
        "posts/create/",
        InternshipPostCreate.as_view(),
        name="Student Posts Create",
    ),
    path(
        "posts/<int:pk>",
        InternshipPostDetail.as_view(),
        name="Student Posts Details",
    ),
    path(
        "posts/update/<int:pk>",
        InternshipPostUpdate.as_view(),
        name="Student Posts Update",
    ),
    path(
        "posts/delete/<int:pk>",
        InternshipPostDelete.as_view(),
        name="Student Posts Delete",
    ),
    # Viewsets
    path(
        "",
        include(router.urls),
    ),
]
