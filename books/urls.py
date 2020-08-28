from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^$', views.BookList.as_view(), name='book_list'),
    url(r'^view/(?P<pk>\d+)/$', views.BookView.as_view(), name='book_view'),
    url(r'^new$', views.BookCreate.as_view(), name='book_new'),
    url(r'^edit/(?P<pk>\d+)/$', views.BookUpdate.as_view(), name='book_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.BookDelete.as_view(), name='book_delete'),
]
'''
url(r'^upload-documents/(?P<pk>\d{0,50})/$', UploadDocumentView.as_view(), name='upload docuemnt'),

path('', views.book_list, name='book_list'),
    path('view/<int:pk>', views.book_view, name='book_view'),
    path('new', views.book_create, name='book_new'),
    path('edit/<int:pk>', views.book_update, name='book_edit'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),
    
    
'''