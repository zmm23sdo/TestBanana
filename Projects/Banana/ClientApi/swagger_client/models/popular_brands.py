# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PopularBrands(object):
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
        'popular_brands': 'list[PopularBrand]'
    }

    attribute_map = {
        'popular_brands': 'popularBrands'
    }

    def __init__(self, popular_brands=None):  # noqa: E501
        """PopularBrands - a model defined in Swagger"""  # noqa: E501
        self._popular_brands = None
        self.discriminator = None
        self.popular_brands = popular_brands

    @property
    def popular_brands(self):
        """Gets the popular_brands of this PopularBrands.  # noqa: E501


        :return: The popular_brands of this PopularBrands.  # noqa: E501
        :rtype: list[PopularBrand]
        """
        return self._popular_brands

    @popular_brands.setter
    def popular_brands(self, popular_brands):
        """Sets the popular_brands of this PopularBrands.


        :param popular_brands: The popular_brands of this PopularBrands.  # noqa: E501
        :type: list[PopularBrand]
        """
        if popular_brands is None:
            raise ValueError("Invalid value for `popular_brands`, must not be `None`")  # noqa: E501

        self._popular_brands = popular_brands

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
        if issubclass(PopularBrands, dict):
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
        if not isinstance(other, PopularBrands):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
