from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from article.viewsets import ArticleViewSet
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)

urlpatterns = [
 path('admin/', admin.site.urls),
 path('api/', include(router.urls)),
 path('', TemplateView.as_view(template_name='index.html')),
]
