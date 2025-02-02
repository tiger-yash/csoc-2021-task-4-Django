from django.urls import path
from store.views import *
from authentication.views import *

urlpatterns = [
    path('', index, name="index"),
    path('books/', bookListView, name="book-list"),
    path('book/<int:bid>/', bookDetailView, name='book-detail'),
    path('books/loaned/', viewLoanedBooks, name="view-loaned"),
    path('books/loan/', loanBookView, name="loan-book"),
    path('books/return/', returnBookView, name="return-book"),
    path('book/<int:bid>/rating/', rateBookView, name="rate-book"),
]
