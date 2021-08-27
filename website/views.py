from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView, ListView, DetailView

from website.models import Post, Category, Tag

# Create your views here.
class IndexView(TemplateView):
    template_name = "home.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "匿名希望"
        ctxt["numservices"] = 200000000
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["numservices"] = 200000000
        ctxt["affiliation"] = [
            "大阪大学大学院基礎工学研究科社会システム数理領域",
            "専攻：機械学習, ファジィ推論, 意思決定論",
            "第21回こいや祭り実行委員会 会計 広報HP担当",
            "18th 祭楽人"
        ]
        ctxt["skills"] = [
            "python",
            "django",
            "C",
            "C++",
            "HTML",
            "CSS, SCSS",
            "PHP",
            "Javascript, jQuery, Nodejs",
            "MySQL",
            "Ruby on Rails",
        ]
        return ctxt

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        return ctxt



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'


class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))


class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))

class CategoryPostView(ListView):
    model = Post
    template_name = 'blog/category_post.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class TagPostView(ListView):
    model = Post
    template_name = 'blog/tag_post.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context