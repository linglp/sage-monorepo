# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from schematic_api.models.basic_error import BasicError  # noqa: E501
from schematic_api.models.components_inner import ComponentsInner  # noqa: E501
from schematic_api.models.dataset_ids_inner import DatasetIdsInner  # noqa: E501
from schematic_api.models.manifests_page import ManifestsPage  # noqa: E501
from schematic_api.test import BaseTestCase


class TestManifestsController(BaseTestCase):
    """ManifestsController integration test stubs"""

    def test_get_manifests(self):
        """Test case for get_manifests

        Facilitate manifest generation
        """
        query_string = [('schemaUrl', 'schema_url_example'),
                        ('title', 'title_example'),
                        ('components', [schematic_api.ComponentsInner()]),
                        ('useAnnotations', False),
                        ('datasetIds', [schematic_api.DatasetIdsInner()]),
                        ('assetViewId', 'asset_view_id_example'),
                        ('strictValidation', True),
                        ('outputFormat', ['output_format_example'])]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/manifests',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
