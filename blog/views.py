from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, \
    TodayArchiveView

from blog.forms import PostSearchForm
from blog.models import Post
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modified'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modified'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modified'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modified'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modified'


class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        sch_word = str(self.request.POST['search_word'])
        post_list = Post.objects.filter(Q(title__icontains=sch_word) |
                                        Q(description__icontains=sch_word) |
                                        Q(content__icontains=sch_word)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = sch_word

        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
