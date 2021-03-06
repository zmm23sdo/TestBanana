# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AddressListReq(object):
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
        'cursor': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'cursor': 'cursor',
        'per_page': 'per_page'
    }

    def __init__(self, cursor=None, per_page=None):  # noqa: E501
        """AddressListReq - a model defined in Swagger"""  # noqa: E501
        self._cursor = None
        self._per_page = None
        self.discriminator = None
        self.cursor = cursor
        self.per_page = per_page

    @property
    def cursor(self):
        """Gets the cursor of this AddressListReq.  # noqa: E501

         游标  # noqa: E501

        :return: The cursor of this AddressListReq.  # noqa: E501
        :rtype: int
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this AddressListReq.

         游标  # noqa: E501

        :param cursor: The cursor of this AddressListReq.  # noqa: E501
        :type: int
        """
        if cursor is None:
            raise ValueError("Invalid value for `cursor`, must not be `None`")  # noqa: E501

        self._cursor = cursor

    @property
    def per_page(self):
        """Gets the per_page of this AddressListReq.  # noqa: E501

         每页多少  # noqa: E501

        :return: The per_page of this AddressListReq.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this AddressListReq.

         每页多少  # noqa: E501

        :param per_page: The per_page of this AddressListReq.  # noqa: E501
        :type: int
        """
        if per_page is None:
            raise ValueError("Invalid value for `per_page`, must not be `None`")  # noqa: E501

        self._per_page = per_page

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
        if issubclass(AddressListReq, dict):
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
        if not isinstance(other, AddressListReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
