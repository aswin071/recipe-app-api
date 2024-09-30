from unittest.mock import patch  #mocking the db behaviour

from psycopg2 import OperationalError as Psycopg2Error #it is the error getting before connecting the db

from django.core.management import call_command #call the command by name that is testing 
from django.db.utils import OperationalError
from django.test import SimpleTestCase #base test class for testing

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    
    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True  # Mock the check function to return True
        
        # Call the command
        call_command('wait_for_db')
        
        # Check if the mock function was called once
        patched_check.assert_called_once_with(database=['default'])
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep,patched_check):
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]
        
        call_command('wait_for_db')
        
        self.assertEqual(patched_check.call_count,6)
        patched_check.assert_called_with(database=['default'])
        