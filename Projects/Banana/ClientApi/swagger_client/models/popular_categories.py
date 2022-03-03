# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PopularCategories(object):
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
        'popular_categories': 'list[PopularCategory]'
    }

    attribute_map = {
        'popular_categories': 'popularCategories'
    }

    def __init__(self, popular_categories=None):  # noqa: E501
        """PopularCategories - a model defined in Swagger"""  # noqa: E501
        self._popular_categories = None
        self.discriminator = None
        self.popular_categories = popular_categories

    @property
    def popular_categories(self):
        """Gets the popular_categories of this PopularCategories.  # noqa: E501


        :return: The popular_categories of this PopularCategories.  # noqa: E501
        :rtype: list[PopularCategory]
        """
        return self._popular_categories

    @popular_categories.setter
    def popular_categories(self, popular_categories):
        """Sets the popular_categories of this PopularCategories.


        :param popular_categories: The popular_categories of this PopularCategories.  # noqa: E501
        :type: list[PopularCategory]
        """
        if popular_categories is None:
            raise ValueError("Invalid value for `popular_categories`, must not be `None`")  # noqa: E501

        self._popular_categories = popular_categories

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
        if issubclass(PopularCategories, dict):
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
        if not isinstance(other, PopularCategories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other