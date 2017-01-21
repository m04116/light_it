from django.conf.urls import url
from .views import authorization_page, m_page, mess_edit, add_comment, add_comment_2


urlpatterns = [
    url(r'^$', authorization_page, name = 'a_page'),
    url(r'^message/', m_page, name = 'm_page'),
#    url(r'^message/', mess_edit, name = 'm_edit'),
    url(r'^message_edit/(?P<pk>[0-9]+)/$', mess_edit, name = 'm_edit'),
    url(r'^add_comment/(?P<pk>[0-9]+)/$', add_comment, name = 'add_comment'),
    url(r'^add_comment_2/(?P<pk>[0-9]+)/$', add_comment_2, name = 'add_comment_2'),
]
