from django.conf.urls import patterns, url

from music import views

urlpatterns = patterns('',

                       url(r'^$', views.ConsumerPhase, name='cons'),
                       url(r'^index/music/$', views.my_view_that_updates_pieFact, name='test'),

)



