from django.urls import path
from .views import PostList, PostDetail, PostCreate

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем новостям у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='posts'),
   path('<int:pk>', PostDetail.as_view(), name='new'),
   path('create/', PostCreate.as_view(), name='new_create'),

]