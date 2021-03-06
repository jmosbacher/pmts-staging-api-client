# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from xepmts_staging.configuration import Configuration


class VoltageMapVoltages(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'voltage': 'float',
        'pmt_index': 'int'
    }

    attribute_map = {
        'voltage': 'voltage',
        'pmt_index': 'pmt_index'
    }

    def __init__(self, voltage=None, pmt_index=None, local_vars_configuration=None):  # noqa: E501
        """VoltageMapVoltages - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._voltage = None
        self._pmt_index = None
        self.discriminator = None

        self.voltage = voltage
        self.pmt_index = pmt_index

    @property
    def voltage(self):
        """Gets the voltage of this VoltageMapVoltages.  # noqa: E501


        :return: The voltage of this VoltageMapVoltages.  # noqa: E501
        :rtype: float
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """Sets the voltage of this VoltageMapVoltages.


        :param voltage: The voltage of this VoltageMapVoltages.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and voltage is None:  # noqa: E501
            raise ValueError("Invalid value for `voltage`, must not be `None`")  # noqa: E501

        self._voltage = voltage

    @property
    def pmt_index(self):
        """Gets the pmt_index of this VoltageMapVoltages.  # noqa: E501


        :return: The pmt_index of this VoltageMapVoltages.  # noqa: E501
        :rtype: int
        """
        return self._pmt_index

    @pmt_index.setter
    def pmt_index(self, pmt_index):
        """Sets the pmt_index of this VoltageMapVoltages.


        :param pmt_index: The pmt_index of this VoltageMapVoltages.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pmt_index is None:  # noqa: E501
            raise ValueError("Invalid value for `pmt_index`, must not be `None`")  # noqa: E501

        self._pmt_index = pmt_index

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VoltageMapVoltages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VoltageMapVoltages):
            return True

        return self.to_dict() != other.to_dict()
