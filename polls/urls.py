from django.urls import path
from . import views

# add app name to enable multiple applications
app_name = 'polls'
urlpatterns = [
    # path function: route, view, name(optional)
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
