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
from xepmts_staging.models.xenon1t_current_change import Xenon1tCurrentChange  # noqa: E501
from xepmts_staging.rest import ApiException

class TestXenon1tCurrentChange(unittest.TestCase):
    """Xenon1tCurrentChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Xenon1tCurrentChange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts_staging.models.xenon1t_current_change.Xenon1tCurrentChange()  # noqa: E501
        if include_optional :
            return Xenon1tCurrentChange(
                timestamp = '0', 
                detector = 'tpc', 
                experiment = 'xenonnt', 
                pmt_index = 56, 
                old_current = 1.337, 
                new_current = 1.337, 
                operator = '0', 
                comments = '0', 
                id = '0'
            )
        else :
            return Xenon1tCurrentChange(
                timestamp = '0',
                detector = 'tpc',
                experiment = 'xenonnt',
                pmt_index = 56,
                new_current = 1.337,
        )

    def testXenon1tCurrentChange(self):
        """Test Xenon1tCurrentChange"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
