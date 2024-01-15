import os
from typing import Union, Literal

from .constants import BASE_URL, DEFAULT_API_VERSION
from .base_client import APIClient
from . import resources


class TwelveLabs(APIClient):
    engine: resources.Engine
    index: resources.Index

    base_url: str
    api_key: str

    def __init__(
        self,
        api_key: str,
        version: Union[
            str,
            Literal["v1.1", "v1.2"],
        ] = DEFAULT_API_VERSION,
    ) -> None:
        base_url = f"{BASE_URL}/{version}/"
        custom_base_url = os.environ.get("TWELVELABS_BASE_URL")
        if custom_base_url is not None:
            base_url = f"{custom_base_url}/{version}/"

        self.base_url = base_url
        self.api_key = api_key
        super().__init__(base_url, api_key)

        self.engine = resources.Engine(self)
        self.index = resources.Index(self)
        self.search = resources.Search(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        pass
