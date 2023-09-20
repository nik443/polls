from django.urls import path

from . import views


app_name = 'polls' # пространство имен, добавил для того, чтобы в случае если в других приложения были представления с такими же имена как в этом приложении - не создавалось проблем
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetainView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]