from unittest.mock import patch  # mocking the db behavior
from psycopg2 import OperationalError as Psycopg2Error  # error raised before connecting to the DB
from django.core.management import call_command  # to call the management command
from django.db.utils import OperationalError
from django.test import SimpleTestCase  # base test class

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available."""
        patched_check.return_value = True  # mock the check function to return True

        # Call the command
        call_command('wait_for_db')

        # Check if the check function was called once
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')  # Mock the time.sleep to avoid delay
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db with delay and retries."""
        # Simulate errors in the first 5 calls, then success on the 6th call
        patched_check.side_effect = [Psycopg2Error] * 2 + \
                                    [OperationalError] * 3 + [True]

        # Call the command
        call_command('wait_for_db')

        # Check that the check function was called 6 times
        self.assertEqual(patched_check.call_count, 6)

        # Check if the final call was made with the correct argument
        patched_check.assert_called_with(databases=['default'])
