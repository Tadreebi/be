from django.urls import path
from app.api.views import SupervisedByListView, SupervisedByDetailsView

urlpatterns = [
    path(
        "",
        SupervisedByListView.as_view(),
        name="supervised_by_list",
    ),
    path(
        "<int:pk>",
        SupervisedByDetailsView.as_view(),
        name="supervised_by_detail",
    ),
]
