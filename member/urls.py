from django.urls import path, include

from rest_framework.routers import DefaultRouter

from member import views

from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='Swagger Help')

router = DefaultRouter()
router.register('member', views.TeamMemberViewSet, basename='member')


urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', swagger_view),
]
