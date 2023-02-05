"""
aruba AP Scan Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<models.py> drf Models Class File

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            aruba
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================
"""
from django.db import models


class TimestampModel(models.Model):
    """Timestamp Class for created/updated field reuse."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Nested Meta Class."""

        abstract = True


class APScanData(TimestampModel):
    """Wi-Fi access point (AP) scan result data."""

    band = models.CharField(max_length=100, blank=True, default='')
    bssid = models.CharField(max_length=100, blank=True, default='')
    channel = models.CharField(max_length=100, blank=True, default='')
    frequency = models.IntegerField(null=True)
    rates = models.CharField(max_length=100, blank=True, default='')
    rssi = models.IntegerField(null=True)
    security = models.CharField(max_length=100, blank=True, default='')
    ssid = models.CharField(max_length=100, blank=True, default='')
    timestamp = models.IntegerField(null=True)
    vendor = models.CharField(max_length=100, blank=True, default='')
    width = models.CharField(max_length=100, blank=True, default='')


class APScanFile(TimestampModel):
    """Wi-Fi access point (AP) scan result file."""

    file = models.FileField(blank=False, null=False)
