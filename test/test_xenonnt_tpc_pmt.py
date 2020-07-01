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
from xepmts_staging.models.xenonnt_tpc_pmt import XenonntTpcPmt  # noqa: E501
from xepmts_staging.rest import ApiException

class TestXenonntTpcPmt(unittest.TestCase):
    """XenonntTpcPmt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XenonntTpcPmt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts_staging.models.xenonnt_tpc_pmt.XenonntTpcPmt()  # noqa: E501
        if include_optional :
            return XenonntTpcPmt(
                serial_number = '0', 
                manufacturer = '0', 
                location = '0', 
                datasheet = '0', 
                id = '0'
            )
        else :
            return XenonntTpcPmt(
                serial_number = '0',
        )

    def testXenonntTpcPmt(self):
        """Test XenonntTpcPmt"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
