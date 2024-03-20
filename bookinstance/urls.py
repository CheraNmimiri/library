from django.urls import path, re_path
from .views import *


urlpatterns = [
    path("", login_required(BookListView.as_view()), name="booklist"),
    path("book-detail/<int:pk>/", BookDeatail.as_view(), name="bookdetail"),
    re_path(r"^get/$", ListCreateCource.as_view(), name="apilistbook"),
    re_path(r"^update/(?P<pk>\d+)/$", RetriveUpdateDestroy.as_view(), name="apibookupdate"),
    path("mybooks", LoanListView.as_view(), name="mybooks"),
]
