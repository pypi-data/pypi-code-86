# generated by datamodel-codegen:
#   filename:  Organization.schema.json
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class Schema(BaseModel):
    __root__: AnyUrl = Field(..., description='String representing a URI.', title='URI')
