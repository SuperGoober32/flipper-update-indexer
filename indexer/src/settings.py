import os
from pydantic import BaseModel
from typing import List, Union
import pathlib


class Settings(BaseModel):
    port: int
    workers: int
    files_dir: str
    base_url: str
    token: str
    github_org: str
    gelf_host: Union[str, None]
    gelf_port: Union[str, None]
    kubernetes_namespace: Union[str, None]
    kubernetes_app: Union[str, None]
    kubernetes_container: Union[str, None]
    kubernetes_pod: Union[str, None]
    firmware_github_token: Union[str, None]
    firmware_github_repo: str
    private_paths: List[str]


settings = Settings(
    port=8000,
    workers=1,
    files_dir=str(pathlib.Path(__file__).parent.parent.parent / "files"),
    base_url="https://up.momentum-fw.dev/",
    token=os.getenv("INDEXER_TOKEN"),
    github_org="Next-Flip",
    gelf_host=os.getenv("GELF_HOST"),
    gelf_port=os.getenv("GELF_PORT"),
    kubernetes_namespace=os.getenv("KUBERNETES_NAMESPACE"),
    kubernetes_app=os.getenv("KUBERNETES_APP"),
    kubernetes_container=os.getenv("KUBERNETES_CONTAINER"),
    kubernetes_pod=os.getenv("HOSTNAME"),
    firmware_github_token=os.getenv("INDEXER_FIRMWARE_GITHUB_TOKEN"),
    firmware_github_repo="Momentum-Firmware",
    private_paths=["reindex", "uploadfiles", "uploadfilesraw"],
)
