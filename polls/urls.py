from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    # eg: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # eg: /polls/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # eg: /polls/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # eg: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
