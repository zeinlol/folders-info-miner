import json
import pathlib
from typing import Union

from core.arguments import cli_arguments


def write_data(output_file: pathlib.Path, data: Union[dict, list, str]):
    try:
        if cli_arguments.json:
            write_data_to_json_file(output_file, data)
        else:
            write_data_to_file(output_file, data)
        print(f'Data successfully wrote to {output_file}.')
    except (Exception, json.JSONDecodeError, json.JSONDecoder) as err:
        print(f'Error while writing data to {output_file}.\nError: {err}')


def write_data_to_file(output_file: pathlib.Path, data: Union[dict, list, str]):
    with(open(output_file, 'w')) as result_file:
        result_file.write(str(data))


def write_data_to_json_file(output_file: pathlib.Path, data: Union[dict, list, str]):
    with(open(output_file, 'w')) as result_file:
        json.dump(data, result_file, indent=2)
