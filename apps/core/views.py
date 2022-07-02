from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "pages/index.html"


index = Index.as_view()
