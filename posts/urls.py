from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.post_new, name="new-post"),
    path('category/<str:cats>/', views.CategoryView, name="category"),
    path('categories-list', views.CategoriesListView, name="categories-list"),
    path('<slug:slug>', views.post_page, name="page"),
    path('update/<slug:slug>', views.post_update, name="update"),
    path('delete/<slug:slug>/', views.post_delete, name="delete"),
    path('<slug:slug>/comment/', views.create_comment, name="comment"),
]
