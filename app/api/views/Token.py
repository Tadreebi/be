from rest_framework_simplejwt.views import TokenViewBase
from app.api.serializers import TokenSerializer


class TokenView(TokenViewBase):
    serializer_class = TokenSerializer
