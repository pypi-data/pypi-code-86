# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from collections.abc import Mapping, Sequence
from enum import Enum
from typing import Any, Optional, Union

from pydantic import BaseModel


class Species(Enum):
    dog = 'dog'
    cat = 'cat'
    snake = 'snake'


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None
    species: Optional[Species] = None


class User(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Event(BaseModel):
    name: Optional[
        Union[str, float, int, bool, Mapping[str, Any], Sequence[str]]
    ] = None
