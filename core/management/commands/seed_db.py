from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Populate all seeds in fixtures with JSON files';

    def handle(self, *args, **kwargs):
        fixtures_dir = os.path.join(os.getcwd(), 'fixtures');

        if not os.path.exists(fixtures_dir):
            self.stdout.write(self.style.ERROR(f"Fixtures directory '{fixtures_dir}' does not exist."));
            return;

        for fixture_file in os.listdir(fixtures_dir):
            if fixture_file.endswith('.json'):
                fixture_path = os.path.join(fixtures_dir, fixture_file);
                try:
                    call_command('loaddata', fixture_path);
                    self.stdout.write(self.style.SUCCESS(f"Successfully loaded {fixture_file}"));
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Failed to load {fixture_file}: {e}"));