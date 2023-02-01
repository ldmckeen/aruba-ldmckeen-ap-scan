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


class APScanDataSerializer(serializers.ModelSerializer):
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


class APScanFileSerializer(serializers.Serializer):
    """Class to validate APScan File."""

    file = serializers.FileField(read_only=True)

    def create(self, validated_data):
        """AP Scan File creation."""
        return APScanFile(id=None, **validated_data)

    def update(self, instance, validated_data):
        """AP Scan File Update."""
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance

    # class Meta:
    #     """Nested Meta Class."""
    #
    #     model = APScanFile
    #     fields = [
    #         'file'
    #     ]
