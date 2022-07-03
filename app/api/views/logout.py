from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect("%s?next=%s" % (settings.LOGOUT_URL, request.path))
