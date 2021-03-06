# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PopularBrand(object):
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
        'parent_id': 'int',
        'name': 'str',
        'logo': 'list[str]',
        'describe': 'str',
        'order': 'int'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parentId',
        'name': 'name',
        'logo': 'logo',
        'describe': 'describe',
        'order': 'order'
    }

    def __init__(self, id=None, parent_id=None, name=None, logo=None, describe=None, order=None):  # noqa: E501
        """PopularBrand - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._parent_id = None
        self._name = None
        self._logo = None
        self._describe = None
        self._order = None
        self.discriminator = None
        self.id = id
        self.parent_id = parent_id
        self.name = name
        self.logo = logo
        self.describe = describe
        self.order = order

    @property
    def id(self):
        """Gets the id of this PopularBrand.  # noqa: E501

         品牌 id  # noqa: E501

        :return: The id of this PopularBrand.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PopularBrand.

         品牌 id  # noqa: E501

        :param id: The id of this PopularBrand.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this PopularBrand.  # noqa: E501


        :return: The parent_id of this PopularBrand.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this PopularBrand.


        :param parent_id: The parent_id of this PopularBrand.  # noqa: E501
        :type: int
        """
        if parent_id is None:
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this PopularBrand.  # noqa: E501

         品牌名称  # noqa: E501

        :return: The name of this PopularBrand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PopularBrand.

         品牌名称  # noqa: E501

        :param name: The name of this PopularBrand.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def logo(self):
        """Gets the logo of this PopularBrand.  # noqa: E501

         品牌 logo 图片  # noqa: E501

        :return: The logo of this PopularBrand.  # noqa: E501
        :rtype: list[str]
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this PopularBrand.

         品牌 logo 图片  # noqa: E501

        :param logo: The logo of this PopularBrand.  # noqa: E501
        :type: list[str]
        """
        if logo is None:
            raise ValueError("Invalid value for `logo`, must not be `None`")  # noqa: E501

        self._logo = logo

    @property
    def describe(self):
        """Gets the describe of this PopularBrand.  # noqa: E501

         品牌描述  # noqa: E501

        :return: The describe of this PopularBrand.  # noqa: E501
        :rtype: str
        """
        return self._describe

    @describe.setter
    def describe(self, describe):
        """Sets the describe of this PopularBrand.

         品牌描述  # noqa: E501

        :param describe: The describe of this PopularBrand.  # noqa: E501
        :type: str
        """
        if describe is None:
            raise ValueError("Invalid value for `describe`, must not be `None`")  # noqa: E501

        self._describe = describe

    @property
    def order(self):
        """Gets the order of this PopularBrand.  # noqa: E501

         排序 id  # noqa: E501

        :return: The order of this PopularBrand.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PopularBrand.

         排序 id  # noqa: E501

        :param order: The order of this PopularBrand.  # noqa: E501
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
        if issubclass(PopularBrand, dict):
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
        if not isinstance(other, PopularBrand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
