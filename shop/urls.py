from django.urls import path
from shop.views.indexview import IndexView, ClearScoresView, GetScoresView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("", IndexView.as_view(), name='index'),
    path('', IndexView.as_view(), name='index'),
    path('clear_scores/', ClearScoresView.as_view(), name='clear_scores'),
    path('get_scores/', GetScoresView.as_view(), name='get_scores'),

]