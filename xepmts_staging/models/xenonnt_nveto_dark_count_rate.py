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


class XenonntNvetoDarkCountRate(object):
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
        'run_id': 'str',
        'timestamp': 'int',
        'detector': 'str',
        'experiment': 'str',
        'pmt_index': 'int',
        'dcr_mean': 'float',
        'dcr_std_dev': 'float',
        'id': 'str'
    }

    attribute_map = {
        'run_id': 'run_id',
        'timestamp': 'timestamp',
        'detector': 'detector',
        'experiment': 'experiment',
        'pmt_index': 'pmt_index',
        'dcr_mean': 'dcr_mean',
        'dcr_std_dev': 'dcr_std_dev',
        'id': '_id'
    }

    def __init__(self, run_id=None, timestamp=None, detector=None, experiment='xenonnt', pmt_index=None, dcr_mean=None, dcr_std_dev=None, id=None, local_vars_configuration=None):  # noqa: E501
        """XenonntNvetoDarkCountRate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._run_id = None
        self._timestamp = None
        self._detector = None
        self._experiment = None
        self._pmt_index = None
        self._dcr_mean = None
        self._dcr_std_dev = None
        self._id = None
        self.discriminator = None

        if run_id is not None:
            self.run_id = run_id
        if timestamp is not None:
            self.timestamp = timestamp
        self.detector = detector
        self.experiment = experiment
        self.pmt_index = pmt_index
        self.dcr_mean = dcr_mean
        if dcr_std_dev is not None:
            self.dcr_std_dev = dcr_std_dev
        if id is not None:
            self.id = id

    @property
    def run_id(self):
        """Gets the run_id of this XenonntNvetoDarkCountRate.  # noqa: E501


        :return: The run_id of this XenonntNvetoDarkCountRate.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this XenonntNvetoDarkCountRate.


        :param run_id: The run_id of this XenonntNvetoDarkCountRate.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def timestamp(self):
        """Gets the timestamp of this XenonntNvetoDarkCountRate.  # noqa: E501


        :return: The timestamp of this XenonntNvetoDarkCountRate.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XenonntNvetoDarkCountRate.


        :param timestamp: The timestamp of this XenonntNvetoDarkCountRate.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def detector(self):
        """Gets the detector of this XenonntNvetoDarkCountRate.  # noqa: E501


        :return: The detector of this XenonntNvetoDarkCountRate.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this XenonntNvetoDarkCountRate.


        :param detector: The detector of this XenonntNvetoDarkCountRate.  # noqa: E501
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
        """Gets the experiment of this XenonntNvetoDarkCountRate.  # noqa: E501


        :return: The experiment of this XenonntNvetoDarkCountRate.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this XenonntNvetoDarkCountRate.


        :param experiment: The experiment of this XenonntNvetoDarkCountRate.  # noqa: E501
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
        """Gets the pmt_index of this XenonntNvetoDarkCountRate.  # noqa: E501


        :return: The pmt_index of this XenonntNvetoDarkCountRate.  # noqa: E501
        :rtype: int
        """
        return self._pmt_index

    @pmt_index.setter
    def pmt_index(self, pmt_index):
        """Sets the pmt_index of this XenonntNvetoDarkCountRate.


        :param pmt_index: The pmt_index of this XenonntNvetoDarkCountRate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pmt_index is None:  # noqa: E501
            raise ValueError("Invalid value for `pmt_index`, must not be `None`")  # noqa: E501

        self._pmt_index = pmt_index

    @property
    def dcr_mean(self):
        """Gets the dcr_mean of this XenonntNvetoDarkCountRate.  # noqa: E501


        :return: The dcr_mean of this XenonntNvetoDarkCountRate.  # noqa: E501
        :rtype: float
        """
        return self._dcr_mean

    @dcr_mean.setter
    def dcr_mean(self, dcr_mean):
        """Sets the dcr_mean of this XenonntNvetoDarkCountRate.


        :param dcr_mean: The dcr_mean of this XenonntNvetoDarkCountRate.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and dcr_mean is None:  # noqa: E501
            raise ValueError("Invalid value for `dcr_mean`, must not be `None`")  # noqa: E501

        self._dcr_mean = dcr_mean

    @property
    def dcr_std_dev(self):
        """Gets the dcr_std_dev of this XenonntNvetoDarkCountRate.  # noqa: E501


        :return: The dcr_std_dev of this XenonntNvetoDarkCountRate.  # noqa: E501
        :rtype: float
        """
        return self._dcr_std_dev

    @dcr_std_dev.setter
    def dcr_std_dev(self, dcr_std_dev):
        """Sets the dcr_std_dev of this XenonntNvetoDarkCountRate.


        :param dcr_std_dev: The dcr_std_dev of this XenonntNvetoDarkCountRate.  # noqa: E501
        :type: float
        """

        self._dcr_std_dev = dcr_std_dev

    @property
    def id(self):
        """Gets the id of this XenonntNvetoDarkCountRate.  # noqa: E501


        :return: The id of this XenonntNvetoDarkCountRate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XenonntNvetoDarkCountRate.


        :param id: The id of this XenonntNvetoDarkCountRate.  # noqa: E501
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
        if not isinstance(other, XenonntNvetoDarkCountRate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XenonntNvetoDarkCountRate):
            return True

        return self.to_dict() != other.to_dict()
