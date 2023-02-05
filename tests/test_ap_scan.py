"""
Aruba AP Scan Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<test_ap_scan.py> DRF Tests File for AP Scan Endpoints

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Aruba
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================
"""
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from apps.apscan.views import APScanFileViewSet

client = APIClient


@pytest.mark.django_db
def test_geolocate_test():
    """Authentication Error."""
    user = User.objects.create_user(username='test_user')
    file_obj = open('./sample_input/apscan_sample.json.zip', 'rb')
    request = APIRequestFactory().post('/apscan_file/geolocate/', data={'file': file_obj})
    force_authenticate(request, user=user)
    handler = APScanFileViewSet.as_view({'post': 'geolocate'})
    _response = handler(request)
    assert _response.status_code == 200


@pytest.mark.django_db
def test_geolocate_403(auth_error_403_description):
    """Authentication Error."""
    request = APIRequestFactory().post('/apscan_file/geolocate/')
    handler = APScanFileViewSet.as_view({'post': 'geolocate'})
    _response = handler(request)
    assert _response.status_code == 403
    assert str(_response.data) == auth_error_403_description
