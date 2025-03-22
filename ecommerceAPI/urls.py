
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet,SubCategoryViewSet,ProductViewSet
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView


router = DefaultRouter()

#register the viewsets
router.register(r"category",CategoryViewSet,basename="category")
router.register(r"catgeory/subcategory",SubCategoryViewSet,basename="subcategories")
router.register(r"product",ProductViewSet,basename="products")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/schema',SpectacularAPIView.as_view(),name="schema"),
    path('api/schema/docs',SpectacularSwaggerView.as_view(url_name="schema"))
]
