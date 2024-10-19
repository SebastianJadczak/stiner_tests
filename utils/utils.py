import json
from enum import Enum
from pathlib import PurePath
from typing import TypeVar
from dacite import Config, from_dict

T = TypeVar('T')


def _load_json(file_path: str | PurePath, encoding: str = 'utf-8') -> dict | list[dict]:
    with open(file_path, encoding=encoding) as json_file:
        return json.load(json_file)


def _from_dict(data_class: type[T], data: dict) -> T:
    return from_dict(data_class=data_class, data=data, config=Config(cast=[Enum], strict=True))


def get_test_data_from_json(data_class: type[T], file_path: str | PurePath) -> T:
    return _from_dict(data_class=data_class, data=_load_json(file_path))
