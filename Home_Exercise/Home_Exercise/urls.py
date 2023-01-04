
from django.contrib import admin
from django.urls import include , path
from MYApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest/fbvlist/', views.FBV_List),
    path('no_rest/', views.no_rest),
    path('rest/fbvpk<int:pk>/', views.FBV_pk),
    path('rest/get_exercise/', views.get_exercise),
    path('rest/get_advices/', views.get_advices),
]
