# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SkuInfoRes(object):
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
        'name': 'str',
        'pic': 'list[str]',
        'price': 'str',
        'sold': 'str',
        'address': 'str',
        'postage': 'str',
        'sku': 'str',
        'stock': 'int',
        'attrs': 'list[Attr]',
        'optionals': 'list[OptionalSku]',
        'describe': 'object',
        'specification': 'str'
    }

    attribute_map = {
        'name': 'name',
        'pic': 'pic',
        'price': 'price',
        'sold': 'sold',
        'address': 'address',
        'postage': 'postage',
        'sku': 'sku',
        'stock': 'stock',
        'attrs': 'attrs',
        'optionals': 'optionals',
        'describe': 'describe',
        'specification': 'specification'
    }

    def __init__(self, name=None, pic=None, price=None, sold=None, address=None, postage=None, sku=None, stock=None, attrs=None, optionals=None, describe=None, specification=None):  # noqa: E501
        """SkuInfoRes - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._pic = None
        self._price = None
        self._sold = None
        self._address = None
        self._postage = None
        self._sku = None
        self._stock = None
        self._attrs = None
        self._optionals = None
        self._describe = None
        self._specification = None
        self.discriminator = None
        self.name = name
        self.pic = pic
        self.price = price
        self.sold = sold
        self.address = address
        self.postage = postage
        self.sku = sku
        self.stock = stock
        self.attrs = attrs
        self.optionals = optionals
        self.describe = describe
        self.specification = specification

    @property
    def name(self):
        """Gets the name of this SkuInfoRes.  # noqa: E501

         商品名称  # noqa: E501

        :return: The name of this SkuInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SkuInfoRes.

         商品名称  # noqa: E501

        :param name: The name of this SkuInfoRes.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def pic(self):
        """Gets the pic of this SkuInfoRes.  # noqa: E501

         商品图片 (第一个为首图)  # noqa: E501

        :return: The pic of this SkuInfoRes.  # noqa: E501
        :rtype: list[str]
        """
        return self._pic

    @pic.setter
    def pic(self, pic):
        """Sets the pic of this SkuInfoRes.

         商品图片 (第一个为首图)  # noqa: E501

        :param pic: The pic of this SkuInfoRes.  # noqa: E501
        :type: list[str]
        """
        if pic is None:
            raise ValueError("Invalid value for `pic`, must not be `None`")  # noqa: E501

        self._pic = pic

    @property
    def price(self):
        """Gets the price of this SkuInfoRes.  # noqa: E501

         商品价格  # noqa: E501

        :return: The price of this SkuInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SkuInfoRes.

         商品价格  # noqa: E501

        :param price: The price of this SkuInfoRes.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def sold(self):
        """Gets the sold of this SkuInfoRes.  # noqa: E501

         销量  # noqa: E501

        :return: The sold of this SkuInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._sold

    @sold.setter
    def sold(self, sold):
        """Sets the sold of this SkuInfoRes.

         销量  # noqa: E501

        :param sold: The sold of this SkuInfoRes.  # noqa: E501
        :type: str
        """
        if sold is None:
            raise ValueError("Invalid value for `sold`, must not be `None`")  # noqa: E501

        self._sold = sold

    @property
    def address(self):
        """Gets the address of this SkuInfoRes.  # noqa: E501

        ship地址  # noqa: E501

        :return: The address of this SkuInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SkuInfoRes.

        ship地址  # noqa: E501

        :param address: The address of this SkuInfoRes.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def postage(self):
        """Gets the postage of this SkuInfoRes.  # noqa: E501

        邮费  # noqa: E501

        :return: The postage of this SkuInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._postage

    @postage.setter
    def postage(self, postage):
        """Sets the postage of this SkuInfoRes.

        邮费  # noqa: E501

        :param postage: The postage of this SkuInfoRes.  # noqa: E501
        :type: str
        """
        if postage is None:
            raise ValueError("Invalid value for `postage`, must not be `None`")  # noqa: E501

        self._postage = postage

    @property
    def sku(self):
        """Gets the sku of this SkuInfoRes.  # noqa: E501

        选中sku码  # noqa: E501

        :return: The sku of this SkuInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this SkuInfoRes.

        选中sku码  # noqa: E501

        :param sku: The sku of this SkuInfoRes.  # noqa: E501
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501

        self._sku = sku

    @property
    def stock(self):
        """Gets the stock of this SkuInfoRes.  # noqa: E501

        选中sku的库存  # noqa: E501

        :return: The stock of this SkuInfoRes.  # noqa: E501
        :rtype: int
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this SkuInfoRes.

        选中sku的库存  # noqa: E501

        :param stock: The stock of this SkuInfoRes.  # noqa: E501
        :type: int
        """
        if stock is None:
            raise ValueError("Invalid value for `stock`, must not be `None`")  # noqa: E501

        self._stock = stock

    @property
    def attrs(self):
        """Gets the attrs of this SkuInfoRes.  # noqa: E501

        可选参数  # noqa: E501

        :return: The attrs of this SkuInfoRes.  # noqa: E501
        :rtype: list[Attr]
        """
        return self._attrs

    @attrs.setter
    def attrs(self, attrs):
        """Sets the attrs of this SkuInfoRes.

        可选参数  # noqa: E501

        :param attrs: The attrs of this SkuInfoRes.  # noqa: E501
        :type: list[Attr]
        """
        if attrs is None:
            raise ValueError("Invalid value for `attrs`, must not be `None`")  # noqa: E501

        self._attrs = attrs

    @property
    def optionals(self):
        """Gets the optionals of this SkuInfoRes.  # noqa: E501

        可选sku描述  # noqa: E501

        :return: The optionals of this SkuInfoRes.  # noqa: E501
        :rtype: list[OptionalSku]
        """
        return self._optionals

    @optionals.setter
    def optionals(self, optionals):
        """Sets the optionals of this SkuInfoRes.

        可选sku描述  # noqa: E501

        :param optionals: The optionals of this SkuInfoRes.  # noqa: E501
        :type: list[OptionalSku]
        """
        if optionals is None:
            raise ValueError("Invalid value for `optionals`, must not be `None`")  # noqa: E501

        self._optionals = optionals

    @property
    def describe(self):
        """Gets the describe of this SkuInfoRes.  # noqa: E501

        产品描述  # noqa: E501

        :return: The describe of this SkuInfoRes.  # noqa: E501
        :rtype: object
        """
        return self._describe

    @describe.setter
    def describe(self, describe):
        """Sets the describe of this SkuInfoRes.

        产品描述  # noqa: E501

        :param describe: The describe of this SkuInfoRes.  # noqa: E501
        :type: object
        """
        if describe is None:
            raise ValueError("Invalid value for `describe`, must not be `None`")  # noqa: E501

        self._describe = describe

    @property
    def specification(self):
        """Gets the specification of this SkuInfoRes.  # noqa: E501

        产品必要信息  # noqa: E501

        :return: The specification of this SkuInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this SkuInfoRes.

        产品必要信息  # noqa: E501

        :param specification: The specification of this SkuInfoRes.  # noqa: E501
        :type: str
        """
        if specification is None:
            raise ValueError("Invalid value for `specification`, must not be `None`")  # noqa: E501

        self._specification = specification

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
        if issubclass(SkuInfoRes, dict):
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
        if not isinstance(other, SkuInfoRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other