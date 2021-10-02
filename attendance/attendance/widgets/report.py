from datetime import datetime, timedelta

from django.db.models import Sum
from django.urls import reverse


class Report:
    max_cells = 12

    cell_tpl = '<td><a href="{}" target="_blank">{}</a></td>'
    empty_cell_tpl = '<td></td>'
    empty_cell_hour_tpl = '<td class="hours"></td>'
    cell_hour_tpl = '<td class="hours">{}</td>'
    cell_total_tpl = '<td class="hours total">{}</td>'
    date_cell_tpl = '<td class="add"><a href="{}" target="_blank">+</a></td><td class="date">{}</td>'
    row_tpl = '<tr class="{}">{}{}</tr>'
    table_tpl = "<table class='table table-bordered table-striped report'>{}</table>"

    def __init__(self, activities):
        self.date = datetime.now()
        self.activities = activities.all()

        base = datetime.today()
        start_date = datetime.fromisoformat("2021-08-01")
        self.date_range = [base - timedelta(days=x) for x in range((base - start_date).days)]

    def __str__(self):
        return self.create_table()

    def create_table(self):
        rows = [self._create_row(day) for day in self.date_range]
        return self._create_table(rows)

    def _create_row(self, day):
        return self.row_tpl.format(
            'sunday' if day.weekday() == 6 else '',
            self._create_giorno(day),
            self._create_activity_list(day)
        )

    def _create_activity_list(self, day):
        return ''.join(
            self._create_total_cell(day) +
            self._create_activities_cells(day) +
            self._create_row_filler(len(self._create_activities_cells(day)) * 2, self.max_cells)
        )

    def _create_activities_cells(self, day):
        return [
            (self.cell_tpl + self.cell_hour_tpl).format(
                reverse('admin:task_activity_change', args=[a.pk]), a.tags_str(),
                str(a.hours)
            )
            for a in self.activities.filter(date=day).order_by('-hours')
        ]

    def _create_total_cell(self, day):
        aggregate = self.activities.filter(date=day).aggregate(Sum('hours'))
        total_cell = aggregate.get('hours__sum', '')
        return [self.cell_total_tpl.format(total_cell) if total_cell else self.empty_cell_hour_tpl]

    def _create_row_filler(self, n, max_activities):
        return [self.empty_cell_tpl] * (max_activities - n)

    def _create_giorno(self, day):
        isoformat = day.isoformat()[:10]
        return self.date_cell_tpl.format(
            reverse('admin:task_activity_add') + "?date={}&user=1".format(isoformat), isoformat,
        )

    def _create_table(self, rows):
        return self.table_tpl.format("".join(rows))
