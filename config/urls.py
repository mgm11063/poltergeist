from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("searches.urls")),
    path("api/v1/products/", include("products.urls")),
    path("api/v1/activities/", include("activities.urls")),
]
