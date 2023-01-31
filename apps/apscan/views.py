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
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from apps.apscan.models import APScanData
from apps.apscan.serializers import APScanSerializer
from apps.apscan.serializers import GroupSerializer
from apps.apscan.serializers import UserSerializer


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


class APScanViewSet(viewsets.ModelViewSet):
    """API endpoint that allows APScanData to be viewed or edited."""

    queryset = APScanData.objects.all()
    serializer_class = APScanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(methods=['POST'], detail=True, url_path='geolocate',
            url_name='geolocate')
    def geolocate(self, request: Request, *args, **kwargs):
        """Find Geographic location of Sensor Input."""
        # Todo:
        #  - Use pandas to run through data in json file and convert Wifi APscan objects
        #  - into geolocation wifiAccessPoints objects.
        #  - Make Post Request call to geolocation API endpoint
        #  - Use Pandas Dataframes if needed
        #  - Cache results, memcache, reddis etc
        success = False
        geo_response = {'Testing': 1234}

        """
        curl -d @scan_geofied.json -H "Content-Type: application/json" -i
        "https://www.googleapis.com/geolocation/v1/geolocate?key=
        AIzaSyCCK6hPzvUI1_XbDCV4pC1HN_6bneUejYc"
        """
        return Response({'success': success, 'geo_response': geo_response})
