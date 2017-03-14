from django.views.generic import CreateView
from .forms import BlogEntryForm


class CreateBlogEntryView(CreateView):
    form_class = BlogEntryForm
    template_name = 'base.html'
    success_url = '/'
