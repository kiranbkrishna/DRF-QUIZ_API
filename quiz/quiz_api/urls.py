from quiz_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'questions', views.MC_QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
        path('', include(router.urls)),
]