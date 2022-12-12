from django.urls import path

from . import views

app_name = "cv"
urlpatterns = [
  path("<int:idUrl>",views.index, name="index"),
  path("contact",views.contact, name="contact")
]