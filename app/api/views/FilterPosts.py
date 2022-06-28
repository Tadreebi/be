from django_filters import rest_framework as filters
from app.models import InternshipPost


class InternshipsFilter(filters.FilterSet):

    class Meta:
        model = InternshipPost
        fields = ('education', 'industry', 'experience')
