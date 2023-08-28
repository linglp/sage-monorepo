"""Implementation of all endpoints related to manifests"""
import os
from typing import Optional, Union
import pandas as pd
from flask import send_from_directory, Response  # type: ignore

from schematic import CONFIG  # type: ignore
from schematic.manifest.generator import ManifestGenerator  # type: ignore
from schematic.schemas.generator import SchemaGenerator  # type: ignore

from schematic_api.controllers.utils import (
    handle_exceptions,
    get_access_token,
    get_temp_jsonld,
)


def check_dataset_ids_match_data_types(
    data_types: Union[None, list[str]], dataset_ids: Union[None, list[str]]
) -> None:
    """If dataset ids exist,
    make sure that length of dataset ids match the length of data types

    Args:
        data_types (Union[None, list[str]]): a list of dataset types or None
        dataset_ids (Union[None, list[str]]): a list of dataset ids or None

    Raises:
        ValueError: Provide data types for each dataset id
        ValueError: Number of dataset ids do not match the number of data types.
    """
    if dataset_ids:
        if not data_types:
            raise ValueError("Provide data types for each dataset id")

        if len(dataset_ids) != len(data_types):
            raise ValueError(
                "Number of dataset ids do not match "
                + "the number of data types"
                + "Provide a data type for each dataset id"
            )


def check_dataset_ids_contain_empty_val(dataset_ids: Union[None, list[str]]) -> None:
    """check if dataset ids contain empty spaces

    Args:
        dataset_ids (Union[None, list[str]]): a list of dataset ids

    Raises:
        ValueError: Dataset ids contain at least one empty value.
        Please check your input
    """
    if dataset_ids:
        all_valid = all(
            "" == dataset_id or dataset_id.isspace() for dataset_id in dataset_ids
        )
        if not all_valid:
            raise ValueError(
                "Dataset ids contain at least one empty value. Please check your input"
            )


def format_manifest_title(component: str, title: Optional[str]) -> str:
    """format manifest title based on component

    Args:
        component (str): component of manifest
        title (Optional[str]): title of manifest

    Returns:
        str: title of manifest
    """
    if title:
        formated_title = f"{title}.{component}.manifest"
    else:
        formated_title = f"Example.{component}.manifest"
    return formated_title


def create_single_manifest(
    json_ld_file_path: str,
    data_type: str,
    title: Optional[str] = None,
    use_annotations: Optional[bool] = False,
    output_format: Optional[str] = "google_sheet",
    access_token: Optional[str] = None,
    dataset_id: Optional[str] = None,
    strict: Optional[bool] = None,
) -> Union[pd.DataFrame, Response, str]:
    # pylint: disable=too-many-arguments
    """_summary_

    Args:
        title (str): _description_
        json_ld_file_path (str): _description_
        data_type (str): _description_
        use_annotations (bool): _description_
        output_format (Optional[str]): _description_
        access_token (Optional[str]): _description_
        dataset_id (Optional[str]): _description_
        strict (Optional[bool]): _description_

    Returns:
        _type_: _description_
    """
    # get manifest title
    formated_title = format_manifest_title(data_type, title)

    # call Manifest Generator
    manifest_generator = ManifestGenerator(
        path_to_json_ld=json_ld_file_path,
        title=formated_title,
        root=data_type,
        use_annotations=use_annotations,
        alphabetize_valid_values="ascending",
    )

    result = manifest_generator.get_manifest(
        dataset_id=dataset_id,
        output_format=output_format,
        access_token=access_token,
        strict=strict,
    )
    # return an excel file if output_format is set to "excel"
    if output_format == "excel":
        dir_name = os.path.dirname(result)
        file_name = os.path.basename(result)
        mimetype = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        return send_from_directory(
            directory=dir_name,
            path=file_name,
            as_attachment=True,
            mimetype=mimetype,
            max_age=0,
        )

    return result


def create_empty_manifests_for_all_components(
    jsonld: str, title: Optional[str], strict: Optional[bool]
) -> list[str]:
    """create empty manifests for all components
    For this mode, only supports returning manifests in google sheet format.

    Args:
        jsonld (str): _description_
        title (Optional[str]): _description_
        strict (Optional[bool]): _description_

    Raises:
        ValueError: _description_

    Returns:
        list[str]: return a list of google sheet urls
    """
    all_results = []
    schema_generator = SchemaGenerator(path_to_json_ld=jsonld)
    component_digraph = schema_generator.se.get_digraph_by_edge_type(
        "requiresComponent"
    )
    components = component_digraph.nodes()
    for component in components:
        formated_title = format_manifest_title(title=title, component=component)

        # since this is for generating empty manifests,
        # assume using the default value of the following parameters:
        # use_annotations = False
        # access_token = None
        # dataset_id = None
        # output_format = "google_sheet"
        result = create_single_manifest(
            title=formated_title,
            json_ld_file_path=jsonld,
            data_type=component,
            strict=strict,
            output_format="google_sheet",
        )
        # make sure the result is str to bypass mypy
        assert isinstance(result, str)
        all_results.append(result)
    return all_results


@handle_exceptions
def get_manifests(
    schema_url: str,
    title: Optional[str] = None,
    components: Optional[list[str]] = None,
    use_annotations: Optional[bool] = False,
    dataset_ids: Optional[list[str]] = None,
    asset_view_id: Optional[str] = None,
    strict_validation: Optional[bool] = True,
    output_format: Optional[str] = "google_sheet",
) -> Union[list[pd.DataFrame], list[str]]:
    # pylint: disable=too-many-arguments
    """_summary_

    Args:
        schema_url (str): _description_
        title (Optional[str], optional): _description_. Defaults to None.
        components (Optional[list[str]], optional): _description_. Defaults to None.
        use_annotations (Optional[bool], optional): _description_. Defaults to False.
        dataset_ids (Optional[list[str]], optional): _description_. Defaults to None.
        asset_view_id (Optional[str], optional): _description_. Defaults to None.
        strict_validation (Optional[bool], optional): _description_. Defaults to True.
        output_format (Optional[str], optional): _description_. Defaults to "google_sheet".

    Returns:
        _type_: _description_
    """
    access_token = get_access_token()

    # save json-ld to a temporary location
    json_ld_file_path = get_temp_jsonld(schema_url)

    # if data type is not provided, generate empty manifests for all data types.
    # here the only possible output format is google sheet
    # this should return a list of google sheet urls
    if not components:
        empty_manifest_urls = create_empty_manifests_for_all_components(
            jsonld=json_ld_file_path, title=title, strict=strict_validation
        )
        return empty_manifest_urls

    # if dataset ids are provided, make sure that they don't have any errors
    if dataset_ids:
        check_dataset_ids_contain_empty_val(dataset_ids=dataset_ids)
        check_dataset_ids_match_data_types(
            data_types=components, dataset_ids=dataset_ids
        )
        # also update master asset view id if it exists
        if asset_view_id:
            CONFIG.synapse_master_fileview_id = asset_view_id

    # generate manifests for each data types
    all_results = []
    for i, component in enumerate(components):
        # if dataset ids are provided, generate existing manifest:
        if dataset_ids:
            output = create_single_manifest(
                title=title,
                json_ld_file_path=json_ld_file_path,
                data_type=component,
                dataset_id=dataset_ids[i],
                access_token=access_token,
                strict=strict_validation,
                output_format=output_format,
                use_annotations=use_annotations,
            )
        else:
            output = create_single_manifest(
                title=title,
                json_ld_file_path=json_ld_file_path,
                data_type=component,
                strict=strict_validation,
                output_format=output_format,
            )

        # assert isinstance(output, (str, pd.DataFrame))

        all_results.append(output)
    # assert isinstance(all_results, (list[str], pd.DataFrame))
    # assert isinstance(all_results, Union[list[str], list[pd.DataFrame]])
    # assert type(all_results) is list[str] or type(all_results) is list[pd.DataFrame]
    return all_results  # type: ignore
