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
from xepmts_staging.models.inline_response20053 import InlineResponse20053  # noqa: E501
from xepmts_staging.rest import ApiException

class TestInlineResponse20053(unittest.TestCase):
    """InlineResponse20053 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20053
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = xepmts_staging.models.inline_response20053.InlineResponse20053()  # noqa: E501
        if include_optional :
            return InlineResponse20053(
                items = [
                    xepmts_staging.models.xenon1t_afterpulse.Xenon1tAfterpulse(
                        experiment = 'xenonnt', 
                        detector = 'tpc', 
                        pmt_index = 56, 
                        run_id = '0', 
                        timestamp = 56, 
                        start_time = 56, 
                        end_time = 56, 
                        trigger_sigma = 1.337, 
                        total_ap = 1.337, 
                        pe = 1.337, 
                        pe_error = 1.337, 
                        ar_pos = 1.337, 
                        hv = 1.337, 
                        ne_ap = 1.337, 
                        ne_pos = 1.337, 
                        xe_pos = 1.337, 
                        n2_pos = 1.337, 
                        ch4ap = 1.337, 
                        he_ap = 1.337, 
                        ar_ap = 1.337, 
                        doublexe_pos = 1.337, 
                        doublexe_ap = 1.337, 
                        trigger_mean = 1.337, 
                        gain = 1.337, 
                        ch4_pos = 1.337, 
                        n2_ap = 1.337, 
                        xe_ap = 1.337, 
                        pe_pulses = 1.337, 
                        trigger_number = 1.337, 
                        _id = '0', )
                    ]
            )
        else :
            return InlineResponse20053(
        )

    def testInlineResponse20053(self):
        """Test InlineResponse20053"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
