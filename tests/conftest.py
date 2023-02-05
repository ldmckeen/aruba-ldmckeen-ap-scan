"""
aruba AP Scan Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<conftest.py> Configuration File for Pytest

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            aruba
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================
"""
import pytest


@pytest.fixture
def auth_error_403_description():
    """Auth Error Response Description."""
    return "{'detail': ErrorDetail(string='You do not have permission to perform this " \
           "action.', code='permission_denied')}"
