from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogForm, BlogModeratorForm
from blog.models import Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Формирование отображения страницы при создании объекта Блог
    """
    model = Blog
    form_class = BlogForm
    # fields = ('title', 'text', 'image', 'publication')
    success_url = reverse_lazy('blog:blog_list')
    login_url = "/users/login/"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        """
        Формирование  slug
        """
        if form.is_valid():
            new_bl = form.save()
            new_bl.slug = slugify(new_bl.title)
            new_bl.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """
    Формирование отображения страницы при обновлении объекта Блог
    """
    model = Blog
    form_class = BlogForm

    # fields = ('title', 'text', 'image', 'publication')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('blog.can_edit_title') and user.has_perm(
                'blog.can_edit_text') and user.has_perm(
                'blog.can_edit_publication'):
            return BlogModeratorForm
        raise PermissionDenied


class BlogDeleteView(DeleteView):
    """
    Формирование отображения страницы при удалении объекта Блог
    """
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    """
    Просмотр на странице всех объектов Блог
    """
    model = Blog

    def get_queryset(self):
        """
        Фильтрация объектов по признаку публикации
        """
        return super().get_queryset().filter(publication=True)


class BlogDetailView(DetailView):
    """
    Детальный просмотр объекта Блог
    """
    model = Blog

    def get_object(self, queryset=None):
        """
        Формирование счетчика просмотров
        """
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object
