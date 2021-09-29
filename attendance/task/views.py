from django.db.models import Sum, F
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.views import generic, View

from attendance.widgets import Report
from task.models import Activity, Tag


class CalendarView(generic.ListView):
    model = Activity
    template_name = 'task/calendar.html'

    def get_context_data(self, **kwargs):
        this_month = timezone.now()
        activities = Activity.objects.all()
        context = super().get_context_data(**kwargs)
        context['report'] = mark_safe(Report(this_month, activities=activities))
        return context


def pie_chart(title, records):
    return {
        'title': title,
        'labels': [r.get('text') for r in records],
        'data': [float(r.get('hours')) for r in records],
    }


class HoursReport(generic.ListView):
    model = Tag
    template_name = 'task/hours.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report_tag'] = self.get_activity_report()

        project_report = self.get_project_report()
        context['report_projects'] = project_report
        context['report_projects_data'] = pie_chart('Progetti', project_report)
        return context

    def get_project_report(self):
        return Tag.objects \
            .filter(activities__project__isnull=False) \
            .annotate(projectname=F('activities__project__name')) \
            .values('projectname') \
            .annotate(text=F('projectname')) \
            .annotate(hours=Sum('activities__hours')) \
            .order_by('-hours')

    def get_activity_report(self):
        return Tag.objects \
            .filter(activities__isnull=False) \
            .values('text') \
            .annotate(hours=Sum('activities__hours')) \
            .order_by('-hours')
