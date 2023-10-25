# coding: utf-8

"""
    OpenChallenges REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ChallengeSubmissionType(str, Enum):
    """
    The submission type of the challenge.
    """

    """
    allowed enum values
    """
    CONTAINER_IMAGE = 'container_image'
    PREDICTION_FILE = 'prediction_file'
    NOTEBOOK = 'notebook'
    OTHER = 'other'

    @classmethod
    def from_json(cls, json_str: str) -> ChallengeSubmissionType:
        """Create an instance of ChallengeSubmissionType from a JSON string"""
        return ChallengeSubmissionType(json.loads(json_str))


