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
from xepmts_staging.models.inline_response20036 import InlineResponse20036  # noqa: E501
from xepmts_staging.rest import ApiException

class TestInlineResponse20036(unittest.TestCase):
    """InlineResponse20036 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20036
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts_staging.models.inline_response20036.InlineResponse20036()  # noqa: E501
        if include_optional :
            return InlineResponse20036(
                items = [
                    xepmts_staging.models.xenonnt_tpc_gain.XenonntTpcGain(
                        run_id = '0', 
                        timestamp = 56, 
                        detector = 'tpc', 
                        experiment = 'xenonnt', 
                        pmt_index = 56, 
                        gain = 1.337, 
                        gain_err = 1.337, 
                        occup = 1.337, 
                        occup_err = 1.337, 
                        _id = '0', )
                    ]
            )
        else :
            return InlineResponse20036(
        )

    def testInlineResponse20036(self):
        """Test InlineResponse20036"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()