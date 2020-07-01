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
import datetime

import xepmts_staging
from xepmts_staging.models.xenon1t_muveto_voltage_map import Xenon1tMuvetoVoltageMap  # noqa: E501
from xepmts_staging.rest import ApiException

class TestXenon1tMuvetoVoltageMap(unittest.TestCase):
    """Xenon1tMuvetoVoltageMap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Xenon1tMuvetoVoltageMap
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts_staging.models.xenon1t_muveto_voltage_map.Xenon1tMuvetoVoltageMap()  # noqa: E501
        if include_optional :
            return Xenon1tMuvetoVoltageMap(
                name = '0', 
                experiment = 'xenonnt', 
                detector = 'tpc', 
                voltages = [
                    xepmts_staging.models.voltage_map_voltages.VoltageMap_voltages(
                        voltage = 1.337, 
                        pmt_index = 56, )
                    ], 
                created_by = '0', 
                comments = '0', 
                date = '0', 
                id = '0'
            )
        else :
            return Xenon1tMuvetoVoltageMap(
                name = '0',
                experiment = 'xenonnt',
                detector = 'tpc',
        )

    def testXenon1tMuvetoVoltageMap(self):
        """Test Xenon1tMuvetoVoltageMap"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
