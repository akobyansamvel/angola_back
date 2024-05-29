from rest_framework.routers import DefaultRouter
from authentication.views import UserViewSet
from hospital.views import HospitalViewSet
from doctor.views import DoctorViewSet
from passport.views import PassportViewSet
from med_insurance.views import MedInsuranceViewSet

router = DefaultRouter()

router.register("user", UserViewSet)
router.register("hospital", HospitalViewSet)
router.register("doctor", DoctorViewSet)
router.register("pasport", PassportViewSet)
router.register("insurance", MedInsuranceViewSet)