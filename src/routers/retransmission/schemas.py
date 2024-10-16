from typing import Union, Any

from pydantic import RootModel

class AnyJson(RootModel):
    root: Union[dict[str, Any], list[dict[str, Any]]]
