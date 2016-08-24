from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter(schema_title='Pastebin API')
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API endpoints
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]