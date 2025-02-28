from app.viewset import StudentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'studentapi', StudentViewSet, basename='student')
urlpatterns = router.urls