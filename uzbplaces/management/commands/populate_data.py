from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = "Populate database with default latest places data."
    requires_migrations_checks = True
    requires_system_checks = True

    def handle(self, *args, **options):
        call_command("loaddata", "places.json", app_label="uzbplaces")