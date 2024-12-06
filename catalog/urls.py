from django.urls import path
from . import views
from django.conf.urls import url
from .views import lastBooks


urlpatterns = [

    path('books/', views.BookListView.as_view(), name='books'),
    path('book-detail/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('book/<int:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('usersbooks/', views.LoanedBooksByStaffListView.as_view(), name='users-borrowed'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('', views.lastBooks, name='index'),
]