from django.urls import path,include
from .views import homeview,detailview,form,delete,edit

urlpatterns = [
    path('',homeview.as_view(),name='home'),
    path('article/<int:pk>', detailview.as_view(), name='article'),
    path('add_post', form.as_view(), name='add_post'),
    path('article/<int:pk>/delete', delete.as_view(), name='delete'),
    path('article/<int:pk>/edit', edit.as_view(), name='edit'),

]
