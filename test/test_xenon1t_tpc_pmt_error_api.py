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
from xepmts_staging.api.xenon1t_tpc_pmt_error_api import Xenon1tTpcPmtErrorApi  # noqa: E501
from xepmts_staging.rest import ApiException


class TestXenon1tTpcPmtErrorApi(unittest.TestCase):
    """Xenon1tTpcPmtErrorApi unit test stubs"""

    def setUp(self):
        self.api = xepmts_staging.api.xenon1t_tpc_pmt_error_api.Xenon1tTpcPmtErrorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_xenon1t_tpc_pmt_errors(self):
        """Test case for get_xenon1t_tpc_pmt_errors

        Retrieves one or more Xenon1tTpcPmtErrors  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
