from django.urls import path, include
from . import views

urlpatterns = [
   path("", views.blog_index, name="blog_index"),
   path("blog/", include("blog.urls")),
   path("<int:pk>/", views.blog_detail, name="blog_detail"),
   path("<category>/", views.blog_category, name="blog_category"),
]
