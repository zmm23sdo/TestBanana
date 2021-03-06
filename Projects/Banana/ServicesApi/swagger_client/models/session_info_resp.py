# coding: utf-8

"""

    认证服务后台api  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SessionInfoResp(object):
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
        'uuid': 'int',
        'tenant': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'tenant': 'tenant'
    }

    def __init__(self, uuid=None, tenant=None):  # noqa: E501
        """SessionInfoResp - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._tenant = None
        self.discriminator = None
        self.uuid = uuid
        self.tenant = tenant

    @property
    def uuid(self):
        """Gets the uuid of this SessionInfoResp.  # noqa: E501


        :return: The uuid of this SessionInfoResp.  # noqa: E501
        :rtype: int
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this SessionInfoResp.


        :param uuid: The uuid of this SessionInfoResp.  # noqa: E501
        :type: int
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def tenant(self):
        """Gets the tenant of this SessionInfoResp.  # noqa: E501


        :return: The tenant of this SessionInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this SessionInfoResp.


        :param tenant: The tenant of this SessionInfoResp.  # noqa: E501
        :type: str
        """
        if tenant is None:
            raise ValueError("Invalid value for `tenant`, must not be `None`")  # noqa: E501

        self._tenant = tenant

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
        if issubclass(SessionInfoResp, dict):
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
        if not isinstance(other, SessionInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
