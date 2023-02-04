
from django.contrib import admin
from django.urls import path, include 



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/tasks/', include('api.v1.tasks.urls')),
    path('api/v1/auth/', include('api.v1.auth.urls')),
    path('tasks/', include('tasks.urls')),

    



]
  