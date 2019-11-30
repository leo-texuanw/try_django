from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article


class ArticleObjectMixin(object):
    model = Article

    def get_object(self):
        id_ = self.kwargs.get("id")
        obj = None
        if id_:
            obj = get_object_or_404(Article, id=id_)
        return obj


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()


    # rediction after creation is currently done in models
    #   by method: get_absolute_url()  # works pretty well
    # But also could be down with the following two ways:
    # 1. success_url = '...'
    # 2.
    # def get_success_url(self):
    #     return '...'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        """ optional """
        form = ArticleModelForm()
        context = {"form": form}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ optional """
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ArticleModelForm()
        context = {"form": form}

        return render(request, self.template_name, context)


class ArticleListView(ListView):
    # This by default look for <blog>/<modelname>_list.html
    # if you want to rewrite default template
    # uncomment next line :
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

    def get_queryset(self):
        """ Optional function """
        return self.queryset


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(ArticleObjectMixin, UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    # minmum:
    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Article, id=id_)

    # Because of ArticleObjectMixin
    def get_object(self):
        id_ = self.kwargs.get("id")
        obj = None
        if id_:
            obj = get_object_or_404(Article, id=id_)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        """ optional """
        context = {}
        obj = self.get_object()
        if obj:
            form = ArticleModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        """ optional """
        context = {}
        obj = self.get_object()
        if obj:
            form = ArticleModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                self.template_name = "articles/article_detail.html"

            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')
