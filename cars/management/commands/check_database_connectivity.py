from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError, DatabaseError


class Command(BaseCommand):
    help = 'Check whether the database accepts connections'
    requires_system_checks = False

    def handle(self, *args, **options):
        db_conn = connections['default']
        try:
            db_conn.cursor()
            
        except DatabaseError as err:
            raise CommandError('Database is not available yet: ' + str(err))
        except OperationalError as err:
            raise CommandError('Database is not available yet: ' + str(err))
        else:
            print("Database is alive")
