from rest_framework import routers

from file_management.views import FileViewSet

router = routers.DefaultRouter()

router.register(r'files', FileViewSet)
