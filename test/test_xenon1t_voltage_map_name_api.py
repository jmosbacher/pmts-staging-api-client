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
from xepmts_staging.api.xenon1t_voltage_map_name_api import Xenon1tVoltageMapNameApi  # noqa: E501
from xepmts_staging.rest import ApiException


class TestXenon1tVoltageMapNameApi(unittest.TestCase):
    """Xenon1tVoltageMapNameApi unit test stubs"""

    def setUp(self):
        self.api = xepmts_staging.api.xenon1t_voltage_map_name_api.Xenon1tVoltageMapNameApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_xenon1t_voltage_map_names(self):
        """Test case for get_xenon1t_voltage_map_names

        Retrieves one or more Xenon1tVoltageMapNames  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
