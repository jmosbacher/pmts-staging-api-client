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
from xepmts_staging.models.inline_response20079 import InlineResponse20079  # noqa: E501
from xepmts_staging.rest import ApiException

class TestInlineResponse20079(unittest.TestCase):
    """InlineResponse20079 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20079
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts_staging.models.inline_response20079.InlineResponse20079()  # noqa: E501
        if include_optional :
            return InlineResponse20079(
                items = [
                    xepmts_staging.models.xenonnt_nveto_install.XenonntNvetoInstall(
                        uid = '0', 
                        array = 'top', 
                        detector = 'tpc', 
                        experiment = 'xenonnt', 
                        pmt_index = 56, 
                        sector = 56, 
                        position_x = 1.337, 
                        position_y = 1.337, 
                        position_z = 1.337, 
                        position_r = 1.337, 
                        amplifier_crate = 56, 
                        amplifier_fan = 56, 
                        amplifier_plug = 56, 
                        amplifier_serial = 56, 
                        amplifier_slot = 56, 
                        amplifier_channel = 56, 
                        digitizer_channel = 56, 
                        digitizer_crate = 56, 
                        digitizer_module = 56, 
                        digitizer_slot = 56, 
                        high_voltage_crate = 56, 
                        high_voltage_board = 56, 
                        high_voltage_channel = 56, 
                        high_voltage_connector = 56, 
                        high_voltage_feedthrough = '0', 
                        high_voltage_return = 56, 
                        serial_number = '0', 
                        signal_channel = 56, 
                        signal_connector = 56, 
                        signal_feedthrough = '0', 
                        _id = '0', )
                    ]
            )
        else :
            return InlineResponse20079(
        )

    def testInlineResponse20079(self):
        """Test InlineResponse20079"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
