from .models import Post
from django_filters import DateFilter, CharFilter, FilterSet
from django import forms


# filter (set of own filters in model Post)
class PostFilter(FilterSet):
    date_time__gt = DateFilter(field_name='time_in',
                               widget=forms.DateInput(attrs={'type': 'date'}),
                               lookup_expr='gt',
                               label='Published after')

    author_relation = CharFilter(field_name='author__user__username',
                                 lookup_expr='icontains',
                                 label='Автор')
    post_title = CharFilter(field_name='title',
                            lookup_expr='icontains',
                            label='Заголовок')

    class Meta:
        model = Post
        fields = ['title']
