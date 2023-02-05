"""
Aruba AP Scan Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<serializers.py> DRF Serializers File

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Aruba
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================
"""
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.apscan.models import APScanData
from apps.apscan.models import APScanFile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate User Data."""

    class Meta:
        """Nested Meta Class."""

        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate Group Data."""

    class Meta:
        """Nested Meta Class."""

        model = Group
        fields = ['url', 'name']


class APScanDataSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate APScan Data."""

    class Meta:
        """Nested Meta Class."""

        model = APScanData
        fields = [
            'band',
            'bssid',
            'channel',
            'frequency',
            'rates',
            'rssi',
            'security',
            'ssid',
            'timestamp',
            'vendor',
            'width'
        ]


class APScanFileSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate APScan File."""

    class Meta:
        """Nested Meta Class."""

        model = APScanFile
        fields = [
            'file'
        ]
