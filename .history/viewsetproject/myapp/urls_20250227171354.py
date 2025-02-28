from myapp.views import StudentViewSet
from rest_framework.routers import DefaultRouter,SimpleRouter
from myapp.views import EmployeeViewSet, TeacherViewSet, CarsViewSet

router = DefaultRouter()
# router = SimpleRouter()
router.register(r'studentapi', StudentViewSet, basename='student')
router.register(r'employeeapi', EmployeeViewSet, basename='employee')
router.register(r'teacherapi', TeacherViewSet, basename='teacher')
router.register(r'carsapi', CarsViewSet, basename='cars')
router.register
urlpatterns = router.urls
