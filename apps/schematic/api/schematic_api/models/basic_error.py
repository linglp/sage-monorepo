# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from schematic_api.models.base_model_ import Model
from schematic_api import util


class BasicError(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, title=None, status=None, detail=None, type=None):  # noqa: E501
        """BasicError - a model defined in OpenAPI

        :param title: The title of this BasicError.  # noqa: E501
        :type title: str
        :param status: The status of this BasicError.  # noqa: E501
        :type status: int
        :param detail: The detail of this BasicError.  # noqa: E501
        :type detail: str
        :param type: The type of this BasicError.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'title': str,
            'status': int,
            'detail': str,
            'type': str
        }

        self.attribute_map = {
            'title': 'title',
            'status': 'status',
            'detail': 'detail',
            'type': 'type'
        }

        self._title = title
        self._status = status
        self._detail = detail
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'BasicError':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BasicError of this BasicError.  # noqa: E501
        :rtype: BasicError
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self):
        """Gets the title of this BasicError.

        A human readable documentation for the problem type  # noqa: E501

        :return: The title of this BasicError.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BasicError.

        A human readable documentation for the problem type  # noqa: E501

        :param title: The title of this BasicError.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def status(self):
        """Gets the status of this BasicError.

        The HTTP status code  # noqa: E501

        :return: The status of this BasicError.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BasicError.

        The HTTP status code  # noqa: E501

        :param status: The status of this BasicError.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this BasicError.

        A human readable explanation specific to this occurrence of the problem  # noqa: E501

        :return: The detail of this BasicError.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this BasicError.

        A human readable explanation specific to this occurrence of the problem  # noqa: E501

        :param detail: The detail of this BasicError.
        :type detail: str
        """

        self._detail = detail

    @property
    def type(self):
        """Gets the type of this BasicError.

        An absolute URI that identifies the problem type  # noqa: E501

        :return: The type of this BasicError.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BasicError.

        An absolute URI that identifies the problem type  # noqa: E501

        :param type: The type of this BasicError.
        :type type: str
        """

        self._type = type
