# generated by datamodel-codegen:
#   filename:  Organization.schema.json
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class Schema(BaseModel):
    __root__: str = Field(..., description='Type of this object.', title='type')
