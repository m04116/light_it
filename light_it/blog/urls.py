from django.conf.urls import url
from .views import authorization_page, m_page, mess_edit


urlpatterns = [
    url(r'^$', authorization_page, name = 'a_page'),
    url(r'^message/', m_page, name = 'm_page'),
#    url(r'^message/', mess_edit, name = 'm_edit'),
    url(r'^message_edit/(?P<pk>[0-9]+)/$', mess_edit, name = 'm_edit'),
]
