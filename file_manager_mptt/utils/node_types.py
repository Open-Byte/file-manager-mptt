

from django.utils.translation import ugettext_lazy as _

## Node Types
FOLDER = 100
FILE = 200

NODE_TYPE = (
    (FILE, _('File')), 
    (FOLDER, _('Folder'))
)

## Fle Type