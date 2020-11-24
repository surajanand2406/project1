from django.urls import path
from blog import views

app_name = 'blog'


urlpatterns = [
	path('index/', views.Index, name='index'),
	path('<int:blog_id>/', views.Detail, name='detail'),
]