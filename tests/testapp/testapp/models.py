from django.db import models
from file_manager_mptt.models import FileMpttModel
from django.utils.translation import ugettext_lazy as _



class FileNodeTestModel(FileMpttModel):
    label = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("File Node Test Model")

