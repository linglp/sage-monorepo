# type: ignore

"""Tests for manifest related endpoints"""

from __future__ import absolute_import
import unittest
from unittest.mock import patch
import pytest

import schematic_api.controllers.manifests_controller_impl
from schematic_api.controllers.manifests_controller_impl import (
    check_dataset_ids_match_data_types,
    check_dataset_ids_contain_empty_val,
    format_manifest_title
)

from schematic_api.test import BaseTestCase

HEADERS = {
    "Accept": "application/json",
    "Authorization": "Bearer xxx",
}

GENERATE_MANIFEST_URL = "/api/v1/manifests?schemaUrl=url1&title=Example \
&components=Patient&useAnnotations=false\
&strictValidation=true&outputFormat=google_sheet"
NODE_DEPENDENCIES_URL = "/api/v1/"


# Improvement: move the following unit tests to schematic library
@pytest.mark.parametrize(
    "data_types, dataset_ids",
    [
        (None, ["dataset_id1"]),
        (["datatype1"], ["dataset_id1"]),
        (["datatype1", "datatype2"], ["dataset_id1", "dataset_id2"]),
    ],
)
def test_check_dataset_ids_match_data_types(data_types, dataset_ids) -> None:
    """Test check_dataset_ids_match_data_types function"""
    # length of dataset ids do not match length of data types
    if dataset_ids and data_types and len(dataset_ids) != len(data_types):
        with pytest.raises(ValueError):
            check_dataset_ids_match_data_types(
                data_types=data_types, dataset_ids=dataset_ids
            )

    # dataset ids are provided but not data types
    if dataset_ids and not data_types:
        with pytest.raises(ValueError):
            check_dataset_ids_match_data_types(
                data_types=data_types, dataset_ids=dataset_ids
            )


@pytest.mark.parametrize(
    "dataset_ids", [None, ["dataset1", None], ["dataset1", " "], ["dataset1", ""]]
)
def test_check_dataset_ids_contain_empty_val(dataset_ids) -> None:
    """Test check_dataset_ids_contain_empty_val function"""
    if dataset_ids:
        with pytest.raises(ValueError):
            check_dataset_ids_contain_empty_val(dataset_ids)

@pytest.mark.parametrize(
    "component, title, expected", [("MockComponent", "Test", "Test.MockComponent.manifest"), ("MockComponent", None, "Example.MockComponent.manifest")]
)
def test_format_manifest_title(component, title, expected):
    """Format titles of manifest"""
    output_title = format_manifest_title(component, title)
    assert output_title == expected

    

# end
class TestManifestGeneration(BaseTestCase):
    """Test case for component attributes endpoint"""

    def test_success(self) -> None:
        """Test for successful result"""

        with patch.object(
            schematic_api.controllers.manifests_controller_impl,
            "get_manifests",
            return_value=["google_sheet_url1"],
        ):
            response = self.client.open(
                GENERATE_MANIFEST_URL, method="GET", headers=HEADERS
            )
            self.assert200(
                response, f"Response body is : {response.data.decode('utf-8')}"
            )

            response_urls = response.json
            assert len(response_urls) == 1
            assert "google_sheet_url1" in response_urls

    def test_500(self) -> None:
        """Test for 500 result"""
        with patch.object(
            schematic_api.controllers.manifests_controller_impl,
            "get_manifests",
            side_effect=TypeError,
        ):
            response = self.client.open(
                GENERATE_MANIFEST_URL, method="GET", headers=HEADERS
            )
            self.assert500(
                response, f"Response body is : {response.data.decode('utf-8')}"
            )


if __name__ == "__main__":
    unittest.main()
