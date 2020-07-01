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
from xepmts_staging.models.inline_response20042 import InlineResponse20042  # noqa: E501
from xepmts_staging.rest import ApiException

class TestInlineResponse20042(unittest.TestCase):
    """InlineResponse20042 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20042
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts_staging.models.inline_response20042.InlineResponse20042()  # noqa: E501
        if include_optional :
            return InlineResponse20042(
                items = [
                    xepmts_staging.models.xenonnt_current_change.XenonntCurrentChange(
                        timestamp = '0', 
                        detector = 'tpc', 
                        experiment = 'xenonnt', 
                        pmt_index = 56, 
                        old_current = 1.337, 
                        new_current = 1.337, 
                        operator = '0', 
                        comments = '0', 
                        _id = '0', )
                    ]
            )
        else :
            return InlineResponse20042(
        )

    def testInlineResponse20042(self):
        """Test InlineResponse20042"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
