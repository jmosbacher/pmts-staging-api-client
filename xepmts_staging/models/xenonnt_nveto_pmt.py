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


class XenonntNvetoPmt(object):
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
        'serial_number': 'str',
        'manufacturer': 'str',
        'location': 'str',
        'datasheet': 'str',
        'id': 'str'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'manufacturer': 'manufacturer',
        'location': 'location',
        'datasheet': 'datasheet',
        'id': '_id'
    }

    def __init__(self, serial_number=None, manufacturer=None, location=None, datasheet=None, id=None, local_vars_configuration=None):  # noqa: E501
        """XenonntNvetoPmt - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._serial_number = None
        self._manufacturer = None
        self._location = None
        self._datasheet = None
        self._id = None
        self.discriminator = None

        self.serial_number = serial_number
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if location is not None:
            self.location = location
        if datasheet is not None:
            self.datasheet = datasheet
        if id is not None:
            self.id = id

    @property
    def serial_number(self):
        """Gets the serial_number of this XenonntNvetoPmt.  # noqa: E501


        :return: The serial_number of this XenonntNvetoPmt.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this XenonntNvetoPmt.


        :param serial_number: The serial_number of this XenonntNvetoPmt.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and serial_number is None:  # noqa: E501
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def manufacturer(self):
        """Gets the manufacturer of this XenonntNvetoPmt.  # noqa: E501


        :return: The manufacturer of this XenonntNvetoPmt.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this XenonntNvetoPmt.


        :param manufacturer: The manufacturer of this XenonntNvetoPmt.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def location(self):
        """Gets the location of this XenonntNvetoPmt.  # noqa: E501


        :return: The location of this XenonntNvetoPmt.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this XenonntNvetoPmt.


        :param location: The location of this XenonntNvetoPmt.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def datasheet(self):
        """Gets the datasheet of this XenonntNvetoPmt.  # noqa: E501


        :return: The datasheet of this XenonntNvetoPmt.  # noqa: E501
        :rtype: str
        """
        return self._datasheet

    @datasheet.setter
    def datasheet(self, datasheet):
        """Sets the datasheet of this XenonntNvetoPmt.


        :param datasheet: The datasheet of this XenonntNvetoPmt.  # noqa: E501
        :type: str
        """

        self._datasheet = datasheet

    @property
    def id(self):
        """Gets the id of this XenonntNvetoPmt.  # noqa: E501


        :return: The id of this XenonntNvetoPmt.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XenonntNvetoPmt.


        :param id: The id of this XenonntNvetoPmt.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, XenonntNvetoPmt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XenonntNvetoPmt):
            return True

        return self.to_dict() != other.to_dict()
