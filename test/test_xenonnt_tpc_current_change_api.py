# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import xepmts_staging
from xepmts_staging.api.xenonnt_tpc_current_change_api import XenonntTpcCurrentChangeApi  # noqa: E501
from xepmts_staging.rest import ApiException


class TestXenonntTpcCurrentChangeApi(unittest.TestCase):
    """XenonntTpcCurrentChangeApi unit test stubs"""

    def setUp(self):
        self.api = xepmts_staging.api.xenonnt_tpc_current_change_api.XenonntTpcCurrentChangeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_xenonnt_tpc_current_changes(self):
        """Test case for get_xenonnt_tpc_current_changes

        Retrieves one or more XenonntTpcCurrentChanges  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()