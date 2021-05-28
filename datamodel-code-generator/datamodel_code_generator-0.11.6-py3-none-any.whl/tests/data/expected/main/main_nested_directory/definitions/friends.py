# generated by datamodel-codegen:
#   filename:  definitions/friends.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field

from . import food


class Friend(BaseModel):
    class Config:
        extra = Extra.allow

    name: str = Field(..., example='John Doe')
    phone_number: Optional[str] = Field(None, example='(555) 555-1234')
    food: Optional[List[Union[food.Noodle, food.Soup]]] = None


class Friends(BaseModel):
    __root__: List[Friend] = Field(..., title='Friends')
