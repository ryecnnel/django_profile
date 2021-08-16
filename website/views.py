from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

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
        ctxt["skills"] = [
            "python",
            "C++",
            "HTML",
            "CSS",
            "PHP",
            "Javascript",
            "MySQL",
            "Ruby",
            "Nodejs",
        ]
        return ctxt

class ContactView(TemplateView):
    template_name = "contact.html"

# ListViewは一覧を簡単に作るためのView
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    #model = Post
    pass

# DetailViewは詳細を簡単に作るためのView
class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    #model = Post
    pass