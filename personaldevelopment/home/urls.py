from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index, name="index"),
    path("manav",views.hello, name="hello"),
    path("anshita",views.anshita, name="hello"),
    # path("admin/", admin.site.urls),
]
