from django.contrib import admin
from django.http import HttpRequest

from .models import Activity, Event, Tag, Project

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

    def get_form(self, request, obj=None, **kwargs):
        form = super(ActivityAdmin, self).get_form(request, obj, **kwargs)
        for k, v in request.GET.items():
            form.base_fields[k].initial = v
        return form


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    save_as = True
    ordering = ('-name',)


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
