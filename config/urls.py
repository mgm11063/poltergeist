from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/products/", include("products.urls")),
    path("api/v1/search/", include("search.urls")),
]
