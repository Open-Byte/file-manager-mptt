import os
import sys
from django.core.management import execute_from_command_line

SITE_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.normpath(os.path.join(SITE_PATH, '..', '..'))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv += ['test']

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testapp.settings")
    execute_from_command_line(sys.argv)