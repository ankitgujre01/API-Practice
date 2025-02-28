from app.viewset import StudentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('studentapi', StudentViewSet, basename='student')
