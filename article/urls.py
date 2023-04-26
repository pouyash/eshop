from django.urls import path

from article import views

urlpatterns = [
    path('',views.ArticleListView.as_view(),name='list_article')
]