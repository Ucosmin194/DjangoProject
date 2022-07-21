from django.urls import path
from book import views

urlpatterns = [
    path('create-new-book/', views.BookCreateView.as_view(), name='create_new_book'),
    path('list-of-books/', views.BookListView.as_view(), name='list_of_books'),
    path('update-book/<int:pk>/', views.BookUpdateView.as_view(), name='update_book'),
    path('details-book/<int:pk>/', views.BookDetailView.as_view(), name='details_book'),
    path('delete-book/<int:pk>/', views.BookDeleteView.as_view(), name='delete_book'),
    path('out-of-stock-book/<int:pk>/', views.out_of_stock_book, name='out_of_stock_book'),

]
