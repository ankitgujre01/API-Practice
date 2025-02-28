from myapp.views import StudentViewSet
from rest_framework.routers import DefaultRouter,SimpleRouter
from myapp

router = DefaultRouter()
# router = SimpleRouter()
router.register(r'studentapi', StudentViewSet, basename='student')
urlpatterns = router.urls
