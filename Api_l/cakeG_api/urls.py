from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'cakeG_api'

urlpatterns = [
	path('',views.index,name='index')
] 