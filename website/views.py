from django.views.generic import TemplateView

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