from dateutils import relativedelta
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.views import generic

from attendance.widgets import Report
from task.models import Activity


class CalendarView(generic.ListView):
    model = Activity
    template_name = 'task/attivita.html'

    def get_context_data(self, **kwargs):
        this_month = timezone.now()
        activities = Activity.objects.all()
        context = super().get_context_data(**kwargs)
        context['report'] = mark_safe(Report(this_month, activities=activities))
        return context
