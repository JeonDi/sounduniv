from django.urls import path
from .views import AboutView, RulesView, DownloadView, LikeView


app_name = 'pages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('rules/', RulesView.as_view(), name='rules'),
    path('download/', DownloadView.as_view(), name='download'),
    path('like/', LikeView.as_view(), name='like'),
]
