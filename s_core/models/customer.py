from django.db import models

from s_core.models.mixins import PersonMixin
from s_core.models.mixins import TimeStampedMixin


class Customer(TimeStampedMixin, PersonMixin):
    mobile_number = models.CharField(max_length=16, null=True, blank=True)
