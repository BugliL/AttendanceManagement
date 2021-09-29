from django.urls import path

from . import views

urlpatterns = [
    path(r'calendar/', views.CalendarView.as_view(), name='calendar'),
    path(r'tag-report/', views.HoursReport.as_view(), name='tags-hours'),
]
