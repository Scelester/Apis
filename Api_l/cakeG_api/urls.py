from django.urls import path,include
from . import views


app_name = 'cakeG_api'

urlpatterns = [
	path('',views.index,name='allcakegapis'),
	path('cakes',views.getCakeData,name="allcakesAPI"),
	path('occation',views.getOccationData,name="alloccationAPI"),
] 