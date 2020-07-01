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


class XenonntMuvetoPmtError(object):
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
        'timestamp': 'str',
        'detector': 'str',
        'experiment': 'str',
        'pmt_index': 'int',
        'error_code': 'int',
        'operator': 'str',
        'details': 'str',
        'comments': 'str',
        'id': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'detector': 'detector',
        'experiment': 'experiment',
        'pmt_index': 'pmt_index',
        'error_code': 'error_code',
        'operator': 'operator',
        'details': 'details',
        'comments': 'comments',
        'id': '_id'
    }

    def __init__(self, timestamp=None, detector=None, experiment='xenonnt', pmt_index=None, error_code=None, operator=None, details=None, comments=None, id=None, local_vars_configuration=None):  # noqa: E501
        """XenonntMuvetoPmtError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._detector = None
        self._experiment = None
        self._pmt_index = None
        self._error_code = None
        self._operator = None
        self._details = None
        self._comments = None
        self._id = None
        self.discriminator = None

        self.timestamp = timestamp
        self.detector = detector
        self.experiment = experiment
        self.pmt_index = pmt_index
        if error_code is not None:
            self.error_code = error_code
        if operator is not None:
            self.operator = operator
        if details is not None:
            self.details = details
        if comments is not None:
            self.comments = comments
        if id is not None:
            self.id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this XenonntMuvetoPmtError.  # noqa: E501


        :return: The timestamp of this XenonntMuvetoPmtError.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XenonntMuvetoPmtError.


        :param timestamp: The timestamp of this XenonntMuvetoPmtError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def detector(self):
        """Gets the detector of this XenonntMuvetoPmtError.  # noqa: E501


        :return: The detector of this XenonntMuvetoPmtError.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this XenonntMuvetoPmtError.


        :param detector: The detector of this XenonntMuvetoPmtError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and detector is None:  # noqa: E501
            raise ValueError("Invalid value for `detector`, must not be `None`")  # noqa: E501
        allowed_values = ["tpc", "nveto", "muveto", "unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and detector not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `detector` ({0}), must be one of {1}"  # noqa: E501
                .format(detector, allowed_values)
            )

        self._detector = detector

    @property
    def experiment(self):
        """Gets the experiment of this XenonntMuvetoPmtError.  # noqa: E501


        :return: The experiment of this XenonntMuvetoPmtError.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this XenonntMuvetoPmtError.


        :param experiment: The experiment of this XenonntMuvetoPmtError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and experiment is None:  # noqa: E501
            raise ValueError("Invalid value for `experiment`, must not be `None`")  # noqa: E501
        allowed_values = ["xenon1t", "xenonnt", "unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and experiment not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `experiment` ({0}), must be one of {1}"  # noqa: E501
                .format(experiment, allowed_values)
            )

        self._experiment = experiment

    @property
    def pmt_index(self):
        """Gets the pmt_index of this XenonntMuvetoPmtError.  # noqa: E501


        :return: The pmt_index of this XenonntMuvetoPmtError.  # noqa: E501
        :rtype: int
        """
        return self._pmt_index

    @pmt_index.setter
    def pmt_index(self, pmt_index):
        """Sets the pmt_index of this XenonntMuvetoPmtError.


        :param pmt_index: The pmt_index of this XenonntMuvetoPmtError.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pmt_index is None:  # noqa: E501
            raise ValueError("Invalid value for `pmt_index`, must not be `None`")  # noqa: E501

        self._pmt_index = pmt_index

    @property
    def error_code(self):
        """Gets the error_code of this XenonntMuvetoPmtError.  # noqa: E501


        :return: The error_code of this XenonntMuvetoPmtError.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this XenonntMuvetoPmtError.


        :param error_code: The error_code of this XenonntMuvetoPmtError.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def operator(self):
        """Gets the operator of this XenonntMuvetoPmtError.  # noqa: E501


        :return: The operator of this XenonntMuvetoPmtError.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this XenonntMuvetoPmtError.


        :param operator: The operator of this XenonntMuvetoPmtError.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def details(self):
        """Gets the details of this XenonntMuvetoPmtError.  # noqa: E501


        :return: The details of this XenonntMuvetoPmtError.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this XenonntMuvetoPmtError.


        :param details: The details of this XenonntMuvetoPmtError.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def comments(self):
        """Gets the comments of this XenonntMuvetoPmtError.  # noqa: E501


        :return: The comments of this XenonntMuvetoPmtError.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this XenonntMuvetoPmtError.


        :param comments: The comments of this XenonntMuvetoPmtError.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def id(self):
        """Gets the id of this XenonntMuvetoPmtError.  # noqa: E501


        :return: The id of this XenonntMuvetoPmtError.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XenonntMuvetoPmtError.


        :param id: The id of this XenonntMuvetoPmtError.  # noqa: E501
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
        if not isinstance(other, XenonntMuvetoPmtError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XenonntMuvetoPmtError):
            return True

        return self.to_dict() != other.to_dict()
