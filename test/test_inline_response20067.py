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
from xepmts_staging.models.inline_response20067 import InlineResponse20067  # noqa: E501
from xepmts_staging.rest import ApiException

class TestInlineResponse20067(unittest.TestCase):
    """InlineResponse20067 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20067
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts_staging.models.inline_response20067.InlineResponse20067()  # noqa: E501
        if include_optional :
            return InlineResponse20067(
                items = [
                    xepmts_staging.models.xenon1t_voltage_map_name.Xenon1tVoltageMapName(
                        name = '0', 
                        _id = '0', )
                    ]
            )
        else :
            return InlineResponse20067(
        )

    def testInlineResponse20067(self):
        """Test InlineResponse20067"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
