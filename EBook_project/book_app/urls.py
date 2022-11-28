
from django.urls import path,include
from .views import CategoryCreateClass,RatingCreate,RatingDetail, CategoryList, CategoryDetail, CreateEbook, EbookList, EbookDetail, EbookDelete,EbookUpdate

urlpatterns = [
    path('category/',CategoryCreateClass.as_view(),name='category-create'),
    path('categorylist/',CategoryList.as_view(),name='category-list'),
    path('category/<int:pk>/',CategoryDetail.as_view(),name='category-detail'),
    path('',CreateEbook.as_view(),name='ebook-create'),
    path('list/',EbookList.as_view(),name='ebook-list'),
    path('list/<int:pk>/',EbookDetail.as_view()),
    path('update/ebook/<int:pk>/',EbookUpdate.as_view(),name='ebook-update'),
    path('delete/<int:pk>/',EbookDelete.as_view(),name='ebook-delete'),
    path('<int:pk>/rate',RatingCreate.as_view(),name='rating-create'), #id the ebook
    path('rating/<int:pk>/',RatingDetail.as_view(),name="rating_detail"), #id is rate id

]
