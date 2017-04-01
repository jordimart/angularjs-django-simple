from django.contrib import admin
from django.conf.urls import include, url
from app.api.v1.routes import api_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # API:V1
    url(r'^api/v1/', include(api_router.urls)),
]