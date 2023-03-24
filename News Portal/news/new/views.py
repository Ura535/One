from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from datetime import datetime
from .filters import PostFilter
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import PostForm
from django.urls import reverse_lazy


class PostList(ListView):

    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'time_in'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    paginate_by = 1 # вот так мы можем указать количество записей

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsList(ListView):
    model = Post
    queryset = Post.objects.filter(typ='NE')
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'new'
    paginate_by = 7


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по новости
    model = Post
    # Используем другой шаблон — post.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'post'

class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'new.add_post'
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        url = self.request.path

        if 'article' in url:
            post.choice = 'AR'
        else:
            post.choice = 'NE'
        return super().form_valid(form)

class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'new.change_post'
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'new.change_post'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')

class CategoryListView(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'category_list.html'
    context_object_name = 'category_list'
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category_relations=self.category)
        self.filterset = PostFilter(self.request.GET, queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['is_not_subscriber'] = self.request.user not in self.category.subscriber.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscriber.add(user)

    message = 'You have successfully subscribed to the newsletter'
    return render(request, 'categories.html', {'category': category, 'message': message})




