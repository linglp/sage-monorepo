# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from schematic_api.models.base_model_ import Model
from schematic_api.models.node_property import NodeProperty
from schematic_api import util

from schematic_api.models.node_property import NodeProperty  # noqa: E501

class NodePropertiesPageAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, node_properties=None):  # noqa: E501
        """NodePropertiesPageAllOf - a model defined in OpenAPI

        :param node_properties: The node_properties of this NodePropertiesPageAllOf.  # noqa: E501
        :type node_properties: List[NodeProperty]
        """
        self.openapi_types = {
            'node_properties': List[NodeProperty]
        }

        self.attribute_map = {
            'node_properties': 'node_properties'
        }

        self._node_properties = node_properties

    @classmethod
    def from_dict(cls, dikt) -> 'NodePropertiesPageAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NodePropertiesPage_allOf of this NodePropertiesPageAllOf.  # noqa: E501
        :rtype: NodePropertiesPageAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def node_properties(self):
        """Gets the node_properties of this NodePropertiesPageAllOf.

        A list of node properties.  # noqa: E501

        :return: The node_properties of this NodePropertiesPageAllOf.
        :rtype: List[NodeProperty]
        """
        return self._node_properties

    @node_properties.setter
    def node_properties(self, node_properties):
        """Sets the node_properties of this NodePropertiesPageAllOf.

        A list of node properties.  # noqa: E501

        :param node_properties: The node_properties of this NodePropertiesPageAllOf.
        :type node_properties: List[NodeProperty]
        """
        if node_properties is None:
            raise ValueError("Invalid value for `node_properties`, must not be `None`")  # noqa: E501

        self._node_properties = node_properties
