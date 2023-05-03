from django.urls import path

from article import views

urlpatterns = [
    path('',views.ArticleListView.as_view(),name='list_article'),
    path('cat/<cat_title>', views.ArticleListView.as_view(), name='article_by_cat'),
    path('detail/<slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('add_comment/',views.add_comment,name='add_comment')
]