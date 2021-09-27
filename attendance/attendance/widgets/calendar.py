from datetime import datetime, timedelta
from calendar import HTMLCalendar


class Calendar(HTMLCalendar):
    def __init__(self, date: datetime, activities):
        self.date = date
        self.activities = activities.filter(date__year=date.year, date__month=date.month)
        super(Calendar, self).__init__()

    def formatday(self, day, weekday):
        d = ''.join('<li>{}</li>'.format(a.format_day()) for a in self.activities.filter(date__day=day))
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek):
        week = ''.join(self.formatday(d, self.activities) for d, weekday in theweek)
        return f'<tr>{week}</tr>'

    def format(self):
        return self.formatmonth(self.date.year, self.date.month)

    def formatmonth(self, theyear, themonth, withyear=True):
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.date.year, self.date.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        cal += '\n'.join(self.formatweek(week) for week in self.monthdays2calendar(self.date.year, self.date.month))
        return cal
