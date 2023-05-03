from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from sweetify import sweetify

from article.models import Article, ArticleComment, ArticleCategoryModel


class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'
    paginate_by = 1
    context_object_name = 'article'
    # def get_queryset(self):
    #     qs = super(ArticleListView, self).get_queryset()
    #     qs=qs.objects.filter(is_active=True)
    #     return qs

    def get_queryset(self):
        qs = super(ArticleListView, self).get_queryset()
        cat_title = self.kwargs.get('cat_title')
        if cat_title:
            qs = qs.filter(categories__title_url__iexact=cat_title)
        return qs


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'
    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article:Article = kwargs.get('object')
        comments = ArticleComment.objects.filter(parent=None, article=article).prefetch_related('parent_comment').order_by('-created_at')
        context['comments'] = comments
        context['comment_count'] = ArticleComment.objects.filter(article=article).count()
        return context

@login_required(login_url='/login')
def add_comment(request:HttpRequest):
    user = request.user
    article_id = request.GET.get('article_id')
    message = request.GET.get('message')
    parent = request.GET.get('parent_id')
    new_message = ArticleComment(article_id=article_id, text=message, user=user,parent_id=parent)
    new_message.save()
    context = {
        'comments' : ArticleComment.objects.filter(article_id=article_id).prefetch_related('parent_comment').order_by('-created_at'),
        'comment_count':ArticleComment.objects.filter(article_id=article_id).count()
    }
    return render(request, 'article/includes/message_box.html', context=context)


def right_side_component(request):
    main_category = ArticleCategoryModel.objects.filter(parent=None)
    context = {
        'main_category':main_category
    }
    return render(request,'article/right_side_component.html',context)














