'''Models for Renewals'''
from django.db import models
from django.conf import settings


VEHICLE_TYPES = (
    ('CAR', 'Car'),
    ('VAN', 'Van'),
)


class Vehicle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vehicles')
    plate = models.CharField(max_length=15)
    nickname = models.CharField(max_length=64, blank=True, null=True)
    colour = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    type = models.CharField(max_length=3, choices=VEHICLE_TYPES)

    def __unicode__(self):
        if self.nickname:
            return '{0} ({1})'.format(self.nickname, self.plate)
        return self.plate


RENEWABLE_TYPES = (
    ('VINS', 'Vehicle Insurance'),
    ('VBRK', 'breakdown cover'),
    ('VMOT', 'MOT'),
    ('CINS', 'Contents Insurance'),
    ('BINS', 'Buildings Insurance'),
    ('OTH', 'Other'),
)


class Renewable(models.Model):

    type = models.CharField(max_length=20, choices=RENEWABLE_TYPES)
    type_other = models.CharField(max_length=200, blank=True, null=True)

    start = models.DateField(blank=True, null=True)
    expires = models.DateField()

    insurer = models.CharField(max_length=100, blank=True, null=True)
    policy_number = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=100, blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, related_name='renewables', blank=True, null=True)
