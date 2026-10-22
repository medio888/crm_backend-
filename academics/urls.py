from rest_framework.routers import DefaultRouter

from .views import FacultyViewSet, DirectionViewSet, GroupViewSet


router = DefaultRouter()
router.register("faculties", FacultyViewSet, basename="faculty")
router.register("directions", DirectionViewSet, basename="direction")
router.register("groups", GroupViewSet, basename="group")

urlpatterns = router.urls
