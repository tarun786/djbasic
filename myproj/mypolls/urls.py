from django.urls import path

from . import views

urlpatterns = [
    path('polls/index.html', views.index,name='index'),
    path('jaiswal',views.jaiswal,name='jaiswal'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('register',views.send_data,name='send_data'),
    path('polls/basetab.html',views.read_all_record,name='read_all_record'),
    path('polls/tarun.html',views.tarun_deatils, name='tarun_details'),
]