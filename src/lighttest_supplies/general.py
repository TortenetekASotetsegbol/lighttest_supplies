from lighttest_supplies.date_methods import get_current_time
from datetime import datetime
from os import makedirs
from pathlib import Path


def boolsum(booleans):
    formated_bools = booleans.values()
    only_true = sum(formated_bools) == len(formated_bools)
    return only_true


def create_logging_structure(*parent_directorie: str) -> Path:
    """
    Create a path for logging directori.

    Arguments:
        parent_directories: one or more parent directory. The argument-order: left to right
    """
    today = datetime.today()
    date_directory_name: str = f'{today.year}_{today.month}_{today.day}'
    hour_name: str = str(today.hour)

    directory_path_components: list[str] = list(parent_directorie)
    directory_path_components.extend([date_directory_name, hour_name])

    unformated_log_directory: str = "/".join(directory_path_components)
    formated_directory_path: Path = Path(unformated_log_directory)
    return formated_directory_path.open()


def create_directory(directory_path: str):
    """
    create a new directory.

    Arguments:
        directory_path: the path of the new directory. format: "C:/parent_directory/child_directory/grandchild_directory
    """
    formatted_directory_path: Path = Path(directory_path)

    try:
        makedirs(formatted_directory_path)
    except FileExistsError as error:
        print("The directory already exist!")
    finally:
        print("directory created!")


def create_logging_directory(*parent_directories: str):
    """
    parent_directories: one or more parent directory. The argument-order: left to right
    """
    full_directory_path: Path = create_logging_structure(*parent_directories)
    try:
        makedirs(full_directory_path)
    except FileExistsError as error:
        print("The directory already exist!")
    finally:
        print("directory created!")


def format_rest_uri(request_url: str) -> str:
    """

    request_url: an endpoint URL

    Return:
        Formatted uri.
    Example:
        format_rest_uri("http://tomcat2.example.hu:8080/example_part1/rest/find/example/information/by/ttt/3100
        -> find/example/information/by/ttt/3100")
    """
    formatted_url: str = request_url.split("rest/")[-1]
    return formatted_url
