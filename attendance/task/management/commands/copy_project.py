from django.core.management.base import BaseCommand, CommandError

from task.models import Project, Project2


class Command(BaseCommand):
    help = 'Copy project to new table'

    def handle(self, *args, **options):
        projects_manager = Project.objects
        projects2_manager = Project2.objects
        projects2_manager.all().delete()

        for p in projects_manager.all():
            p2 = projects2_manager.create(
                name=p.name,
                note=p.note,
            )

            for t in p.tags.all():
                p2.tags.add(t)
                p2.save()

            for a in p.activities.all():
                a.project2 = p2
                a.save()

