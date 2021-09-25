from django.contrib import admin

from .models import Activity, Event, Project, Tag

admin.site.site_header = 'Attendance management'  # default: "Django Administration"
admin.site.index_title = 'Attendance'  # default: "Site administration"
admin.site.site_title = 'Attendance management'  # default: "Django site admin"


class EventAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    save_as = True
    ordering = ('-date',)


class ActivityAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    save_as = True
    ordering = ('-date',)


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project)
admin.site.register(Tag)
