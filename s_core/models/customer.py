from django.db import models

from s_core.models.mixins import PersonMixin
from s_core.models.mixins import TimeStampedMixin
from sarimuson.users.models import User


class Customer(TimeStampedMixin, PersonMixin):
    user = models.OneToOneField(User, related_name='customer', on_delete=models.PROTECT)
    mobile_number = models.CharField(max_length=16, null=True, blank=True)
