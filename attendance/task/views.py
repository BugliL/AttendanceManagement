from datetime import timedelta

from django.utils import timezone
from django.views import generic
from django.utils.safestring import mark_safe
from attendance.widgets.calendar import Calendar
from task.models import Activity
from dateutils import relativedelta


class CalendarView(generic.ListView):
    model = Activity
    template_name = 'task/attivita.html'

    def get_context_data(self, **kwargs):
        this_month = timezone.now()
        last_month = this_month + relativedelta(months=-1)
        next_month = this_month + relativedelta(months=+1)

        activities = Activity.objects.all()
        context = super().get_context_data(**kwargs)
        context['this_month_calendar'] = mark_safe(Calendar(this_month, activities=activities).format())
        context['last_month_calendar'] = mark_safe(Calendar(last_month, activities=activities).format())
        context['next_month_calendar'] = mark_safe(Calendar(next_month, activities=activities).format())

        return context
