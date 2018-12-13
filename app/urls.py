from django.conf.urls import url, include
from . import views
# from . import app

urlpatterns = [
    url(r'^$',views.Dashboard.as_view(),name='home'),


]