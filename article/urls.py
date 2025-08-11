from django.urls import path
from . import views
from .views import (
    ArticleListView, 
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
    like_article,
    download_article_pdf,
)

urlpatterns = [
    # ArticleList Path
    path('list/<str:username>/', ArticleListView.as_view(), name='article_list'),

    # CreateArticle Path
    path('new/', ArticleCreateView.as_view(), name='article_new'),

    # Delete and Edit Article Path
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='article_edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),

    # Like Path
    path('article/<int:pk>/like/', views.like_article, name='like_article'),

    # Download PDF Path
    path('<int:pk>/download-pdf/', download_article_pdf, name='article_download_pdf'),

    # ArticleDetail Path
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail')
]