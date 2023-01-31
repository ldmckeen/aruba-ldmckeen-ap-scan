"""
Aruba AP Scan Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<apps.py> DRF Apps File

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Aruba
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================
"""
from django.apps import AppConfig


class ApScanConfig(AppConfig):
    """Configuration for apscan extending AppConfig."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.apscan'
