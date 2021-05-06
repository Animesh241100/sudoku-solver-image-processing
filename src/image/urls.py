from django.urls import path
from .views import (
  upload_image_view
)

app_name = 'image'

urlpatterns = [
    # path('', home_view, name = 'home_view'),
    path('', upload_image_view, name = 'upload_image'),
    # path('<int:pk>/', article_detail),
    # path('user/list/', user_article_list),
    # path('user/<int:pk>/', user_article_detail),
    # path('search/', ArticleSearchAPIView.as_view())
]