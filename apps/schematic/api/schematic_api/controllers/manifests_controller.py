import connexion

from schematic_api.models.components_inner import ComponentsInner  # noqa: E501
from schematic_api.models.dataset_ids_inner import DatasetIdsInner  # noqa: E501
from schematic_api.controllers import manifests_controller_impl


def get_manifests(
    schema_url,
    title=None,
    components=None,
    use_annotations=None,
    dataset_ids=None,
    asset_view_id=None,
    strict_validation=None,
    output_format=None,
):  # noqa: E501
    """Facilitate manifest generation

    Facilitate manifest generation # noqa: E501

    :param schema_url: The URL of a schema in jsonld form
    :type schema_url: str
    :param title: The title of a manifest
    :type title: str
    :param components: An array of components
    :type components: list | bytes
    :param use_annotations: Whether or not to use annotations
    :type use_annotations: bool
    :param dataset_ids: An array of dataset ids
    :type dataset_ids: list | bytes
    :param asset_view_id: ID of view listing all project data assets. E.g. for Synapse this would be the Synapse ID of the fileview listing all data assets for a given project
    :type asset_view_id: str
    :param strict_validation: Whether or not to use strict validation.
    :type strict_validation: bool
    :param output_format: The output of manifests to return.
    :type output_format: List[str]

    :rtype: Union[ManifestsPage, Tuple[ManifestsPage, int], Tuple[ManifestsPage, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        components = [
            ComponentsInner.from_dict(d) for d in connexion.request.get_json()
        ]  # noqa: E501
    if connexion.request.is_json:
        dataset_ids = [
            DatasetIdsInner.from_dict(d) for d in connexion.request.get_json()
        ]  # noqa: E501
    return manifests_controller_impl.get_manifests(
        schema_url,
        title,
        components,
        use_annotations,
        dataset_ids,
        asset_view_id,
        strict_validation,
        output_format,
    )
