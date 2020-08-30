from django.conf.urls import url
from app_generic_views import views

urlpatterns = [
    url(r'^$', views.BookList.as_view(), name='book_list'),
    url(r'^new/$', views.BookCreate.as_view(), name='book_new'),
]
