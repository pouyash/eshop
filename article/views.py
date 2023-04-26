from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from article.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'
    paginate_by = 1
    context_object_name = 'article'
    # def get_queryset(self):
    #     qs = super(ArticleListView, self).get_queryset()
    #     qs=qs.objects.filter(is_active=True)
    #     return qs