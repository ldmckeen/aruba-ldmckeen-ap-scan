"""
Aruba AP Scan Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<views.py> DRF Views File

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Aruba
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================

Geolocation API with sample data
---------------------------------

{
  "considerIp": "false",
  "wifiAccessPoints": [
    {
      "macAddress": "9c:b2:b2:66:c1:be",
      "signalStrength": -35,
      "signalToNoiseRatio": 20
    },
    {
      "macAddress": "84:78:ac:b9:76:19",
      "signalStrength": -56,
      "signalToNoiseRatio": 20
    },
    {
      "macAddress": "c0:a0:bb:c4:10:d6",
      "signalStrength": -66,
      "signalToNoiseRatio": 40
    }
  ]
}


Our APScan data
---------------------------------

[
  {
    "apscan_data": [
    {
        "band": "2.4",
        "bssid": "9c:b2:b2:66:c1:be",
        "channel": "5",
        "frequency": 2432,
        "rates": "1.0 - 135.0 Mbps",
        "rssi": -35,
        "security": "wpa-psk",
        "ssid": "HUAWEI-B315-C1BE",
        "timestamp": 1522886457.0,
        "vendor": "HUAWEI TECHNOLOGIES CO.,LTD",
        "width": "20"
      },
      {
        "band": "2.4",
        "bssid": "84:78:ac:b9:76:19",
        "channel": "1",
        "frequency": 2412,
        "rates": "6.5 - 270.0 Mbps",
        "rssi": -56,
        "security": "wpa-eap",
        "ssid": "1 Telkom Connect",
        "timestamp": 1522886457.0,
        "vendor": "Cisco Systems, Inc",
        "width": "20"
      },
      {
        "band": "2.4",
        "bssid": "c0:a0:bb:c4:10:d6",
        "channel": "1",
        "frequency": 2412,
        "rates": "1.0 - 54.0 Mbps",
        "rssi": -66,
        "security": "wpa-psk",
        "ssid": "default",
        "timestamp": 1522886457.0,
        "vendor": "D-Link International",
        "width": "40"
      }
    ]
  }
]

Aruba File to Geolocation file mapping
--------------------------------->>>>>>
bssid": "e8:1d:a8:68:a6:6c"    "macAddress": "84:d4:7e:f6:99:64"
"rssi": -82                    "signalStrength": -5
"width": "80"                  "signalToNoiseRatio": 0


Return Example
---------------------------------
{
  "location": {
    "lat": -33.9203736,
    "lng": 25.5912552
  },
  "accuracy": 20.329
}

"""
import json
import logging
from zipfile import ZipFile

import requests
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from requests.exceptions import HTTPError
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from apps.apscan.models import APScanData
from apps.apscan.models import APScanFile
from apps.apscan.serializers import APScanDataSerializer
from apps.apscan.serializers import APScanFileSerializer
from apps.apscan.serializers import GroupSerializer
from apps.apscan.serializers import UserSerializer

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class APScanDataViewSet(viewsets.ModelViewSet):
    """API endpoint that allows APScanData to be viewed or edited."""

    queryset = APScanData.objects.all()
    serializer_class = APScanDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class APScanFileViewSet(viewsets.ModelViewSet):
    """API endpoint that allows APScanData to be viewed or edited."""

    queryset = APScanFile.objects.all()
    serializer_class = APScanFileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(methods=['POST'], detail=False, url_path='geolocate', url_name='geolocate')
    def geolocate(self, request: Request, pk=None, *args, **kwargs):
        """Find Geographic location of Sensor Input."""
        # Setup Dictionary object that will be converted to Json for
        scan_data_geofied = {
            'considerIp': 'false',
            'wifiAccessPoints': []
        }

        # Open the zip file in READ mode
        input_zip = ZipFile(request.data['file'], 'r')
        file_name = input_zip.namelist()[0]
        text = input_zip.read(file_name)
        data = json.loads(text)
        apscan_data = data[0]

        # Map Apscan data to required fields for Google Geolocation API
        for apscan, sensor_data in apscan_data.items():
            for item in sensor_data:
                scan_data_geofied['wifiAccessPoints'].append(
                    {
                        'macAddress': item['bssid'],
                        'signalStrength': item['rssi'],
                        'signalToNoiseRatio': item['width']
                    },
                )

        try:
            response = requests.post(
                url=f'{settings.GEOLOCATE_URL}{settings.GEOLOCATE_KEY}',
                json=scan_data_geofied,
            )
            response.raise_for_status()
            json_response = json.loads(response.content)
            return Response(json_response)
        except HTTPError as ex:
            logger.error(f'services.py: Error in geo location call - {ex}')
            return False
