from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from agenda.form import EventForm
from agenda.models import *


def event_list_json(request):
    return JsonResponse(list(Event.objects.values()), safe=False)

def agenda_view(request):
    return render(request, 'agenda/agenda.html')


class EventView(FormView):
    template_name = 'agenda/event.html'
    success_url = reverse_lazy('index')
    form_class = EventForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.agenda = get_object_or_404(Agenda, user=self.request.user.agenda)
        obj.save()

        return super().form_valid(form)


event_view = EventView.as_view()





# Create your views here.
def calendarView(request):
    return render(request, 'calendar_alphine.html', {
        'form': [a.to_dict() for a in Event.objects.all()],
        # 'activity_form': ActivityForm()
    })


"""
def item_list(request):
    items = Event.objects.all()
    return render(request, 'calendar_alphine.html', {'items': items})


def item_list_json(request):
    items = list(Event.objects.values())
    return JsonResponse(items, safe=False)
"""
