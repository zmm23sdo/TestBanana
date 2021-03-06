# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PopularCategory(object):
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
        'id': 'int',
        'name': 'str',
        'pic': 'list[str]',
        'order': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'pic': 'pic',
        'order': 'order'
    }

    def __init__(self, id=None, name=None, pic=None, order=None):  # noqa: E501
        """PopularCategory - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._pic = None
        self._order = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.pic = pic
        self.order = order

    @property
    def id(self):
        """Gets the id of this PopularCategory.  # noqa: E501

         类别 id  # noqa: E501

        :return: The id of this PopularCategory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PopularCategory.

         类别 id  # noqa: E501

        :param id: The id of this PopularCategory.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this PopularCategory.  # noqa: E501

         类别名称  # noqa: E501

        :return: The name of this PopularCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PopularCategory.

         类别名称  # noqa: E501

        :param name: The name of this PopularCategory.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def pic(self):
        """Gets the pic of this PopularCategory.  # noqa: E501

         类别图片  # noqa: E501

        :return: The pic of this PopularCategory.  # noqa: E501
        :rtype: list[str]
        """
        return self._pic

    @pic.setter
    def pic(self, pic):
        """Sets the pic of this PopularCategory.

         类别图片  # noqa: E501

        :param pic: The pic of this PopularCategory.  # noqa: E501
        :type: list[str]
        """
        if pic is None:
            raise ValueError("Invalid value for `pic`, must not be `None`")  # noqa: E501

        self._pic = pic

    @property
    def order(self):
        """Gets the order of this PopularCategory.  # noqa: E501

         类别排序 id  # noqa: E501

        :return: The order of this PopularCategory.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PopularCategory.

         类别排序 id  # noqa: E501

        :param order: The order of this PopularCategory.  # noqa: E501
        :type: int
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

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
        if issubclass(PopularCategory, dict):
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
        if not isinstance(other, PopularCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
