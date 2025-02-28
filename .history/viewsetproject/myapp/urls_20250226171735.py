from myapp.views import StudentViewSet
from rest_framework.routers import DefaultRouter,SimpleRouter
from myapp.views import EmployeeViewSet

router = DefaultRouter()
# router = SimpleRouter()
router.register(r'studentapi', StudentViewSet, basename='student')
router.register(r'employeeapi', EmployeeViewSet, basename='employee')

urlpatterns = router.urls
