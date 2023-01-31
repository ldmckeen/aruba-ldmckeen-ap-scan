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
        success = False
        geo_response = {'Testing': 1234}
        return Response({'success': success, 'geo_response': geo_response})
