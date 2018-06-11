# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse200ConfigConstantAttributesValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'visible': 'bool',
        'read_only': 'bool'
    }

    attribute_map = {
        'visible': 'visible',
        'read_only': 'readOnly'
    }

    def __init__(self, visible=None, read_only=None):
        """
        InlineResponse200ConfigConstantAttributesValue - a model defined in Swagger
        """

        self._visible = None
        self._read_only = None

        if visible is not None:
          self.visible = visible
        if read_only is not None:
          self.read_only = read_only

    @property
    def visible(self):
        """
        Gets the visible of this InlineResponse200ConfigConstantAttributesValue.

        :return: The visible of this InlineResponse200ConfigConstantAttributesValue.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """
        Sets the visible of this InlineResponse200ConfigConstantAttributesValue.

        :param visible: The visible of this InlineResponse200ConfigConstantAttributesValue.
        :type: bool
        """

        self._visible = visible

    @property
    def read_only(self):
        """
        Gets the read_only of this InlineResponse200ConfigConstantAttributesValue.

        :return: The read_only of this InlineResponse200ConfigConstantAttributesValue.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this InlineResponse200ConfigConstantAttributesValue.

        :param read_only: The read_only of this InlineResponse200ConfigConstantAttributesValue.
        :type: bool
        """

        self._read_only = read_only

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse200ConfigConstantAttributesValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
