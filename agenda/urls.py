from django.urls import re_path
from django.urls import path
from django.views.static import serve

from agenda.views import event_view, agenda_view, event_update_view
from calendarproject import settings

urlpatterns = [
    path(route='', name='index', view=agenda_view),
    path(route='event/new', name='new-event', view=event_view),
    path(route='event/<int:pk>', name='new-event', view=event_update_view),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
