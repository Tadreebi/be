from django_filters import rest_framework as filters
from app.models.InternshipPost import PostInternship

class InternshipsFilter(filters.FilterSet):
    
    class Meta:
        model = PostInternship
        fields = ('education', 'industry', 'experience')