import apps.bookmodule.views
from django.urls import path

urlpatterns = [
    path('', apps.bookmodule.views.home,name="home"), #add only this line of code
    path('index2/<int:val1>', apps.bookmodule.views.index2), #add only this line of code
    path('index3', apps.bookmodule.views.indexwithtamblet), #add only this line of code
    path('showBook/<int:bookId>', apps.bookmodule.views.viewbook),
    path('booklist',apps.bookmodule.views.show,name="BookList"),
    path('oneBook/<int:BId>',apps.bookmodule.views.oneBook,name="OneBook")
]