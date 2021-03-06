# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateCartReq(object):
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
        'product_num': 'int',
        'sku': 'str'
    }

    attribute_map = {
        'product_num': 'product_num',
        'sku': 'sku'
    }

    def __init__(self, product_num=None, sku=None):  # noqa: E501
        """UpdateCartReq - a model defined in Swagger"""  # noqa: E501
        self._product_num = None
        self._sku = None
        self.discriminator = None
        self.product_num = product_num
        self.sku = sku

    @property
    def product_num(self):
        """Gets the product_num of this UpdateCartReq.  # noqa: E501

         商品数量  # noqa: E501

        :return: The product_num of this UpdateCartReq.  # noqa: E501
        :rtype: int
        """
        return self._product_num

    @product_num.setter
    def product_num(self, product_num):
        """Sets the product_num of this UpdateCartReq.

         商品数量  # noqa: E501

        :param product_num: The product_num of this UpdateCartReq.  # noqa: E501
        :type: int
        """
        if product_num is None:
            raise ValueError("Invalid value for `product_num`, must not be `None`")  # noqa: E501

        self._product_num = product_num

    @property
    def sku(self):
        """Gets the sku of this UpdateCartReq.  # noqa: E501

         当前商品数量  # noqa: E501

        :return: The sku of this UpdateCartReq.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this UpdateCartReq.

         当前商品数量  # noqa: E501

        :param sku: The sku of this UpdateCartReq.  # noqa: E501
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501

        self._sku = sku

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
        if issubclass(UpdateCartReq, dict):
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
        if not isinstance(other, UpdateCartReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
