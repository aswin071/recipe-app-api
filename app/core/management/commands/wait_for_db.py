from typing import Any
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

class Command(BaseCommand):
    
    def handle(self, *args: Any, **options: Any):
        self.stdout.write('waiting for database ...')
        db_up=False
        while db_up is False:
            try:
                self.check(database=['default'])  # check if the db is up
                db_up = True
            except (Psycopg2Error,OperationalError):
                self.stdout.write('database not available yet, waiting 5 seconds...')
                time.sleep(1)
                
        self.stdout.write(self.style.SUCCESS('database is available'))
 
                