"""Tests for manifest related endpoints"""

from __future__ import absolute_import
import unittest
from unittest.mock import patch

import schematic_api.controllers.manifests_controller_impl
from schematic_api.test import BaseTestCase

HEADERS = {
    "Accept": "application/json",
    "Authorization": "Bearer xxx",
}

GENERATE_MANIFEST_URL = "/api/v1/manifests?schemaUrl=url1&title=Example \
&components=Patient&useAnnotations=false \
&strictValidation=true&outputFormat=google_sheet"
NODE_DEPENDENCIES_URL = "/api/v1/"


class TestComponentAttributes(BaseTestCase):
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
