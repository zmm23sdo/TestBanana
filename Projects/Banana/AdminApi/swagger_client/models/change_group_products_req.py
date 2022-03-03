# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ChangeGroupProductsReq(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ids': 'list[str]',
        'group_ids': 'list[str]'
    }

    attribute_map = {
        'ids': 'ids',
        'group_ids': 'group_ids'
    }

    def __init__(self, ids=None, group_ids=None):  # noqa: E501
        """ChangeGroupProductsReq - a model defined in Swagger"""  # noqa: E501
        self._ids = None
        self._group_ids = None
        self.discriminator = None
        self.ids = ids
        self.group_ids = group_ids

    @property
    def ids(self):
        """Gets the ids of this ChangeGroupProductsReq.  # noqa: E501

         商品ID集合  # noqa: E501

        :return: The ids of this ChangeGroupProductsReq.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ChangeGroupProductsReq.

         商品ID集合  # noqa: E501

        :param ids: The ids of this ChangeGroupProductsReq.  # noqa: E501
        :type: list[str]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")  # noqa: E501

        self._ids = ids

    @property
    def group_ids(self):
        """Gets the group_ids of this ChangeGroupProductsReq.  # noqa: E501

         分组ID集合  # noqa: E501

        :return: The group_ids of this ChangeGroupProductsReq.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this ChangeGroupProductsReq.

         分组ID集合  # noqa: E501

        :param group_ids: The group_ids of this ChangeGroupProductsReq.  # noqa: E501
        :type: list[str]
        """
        if group_ids is None:
            raise ValueError("Invalid value for `group_ids`, must not be `None`")  # noqa: E501

        self._group_ids = group_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ChangeGroupProductsReq, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChangeGroupProductsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other