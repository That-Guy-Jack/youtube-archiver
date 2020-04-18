import sys
from pathlib import Path
from typing import NamedTuple, Optional, Union

if sys.version_info > (3, 7):
    from typing import Literal, TypedDict
else:
    from mypy_extensions import Literal, TypedDict


class DownloadResult(NamedTuple):
    """Tuple containing all possible outputs from a download request."""

    pretty_name: str
    output_dir: Path
    info_file: Path
    video_file: Optional[Path]
    audio_file: Optional[Path]


class _DownloadedUpdateNoReqID(TypedDict):
    """Realtime update message indicating a file was downloaded."""

    status: Literal["downloaded"]
    filename: Path


class DownloadedUpdate(_DownloadedUpdateNoReqID, total=False):
    """Realtime update message indicating a file was downloaded, with optional `req_id`."""

    req_id: str


class _CompletedUpdateNoReqID(TypedDict):
    """Realtime update message indicating a download request was completed."""

    status: Literal["completed"]
    pretty_name: str
    info_file: Optional[Path]
    video_file: Optional[Path]
    audio_file: Optional[Path]


class CompletedUpdate(_CompletedUpdateNoReqID, total=False):
    """Realtime update message indicating a download request was completed, with optional `req_id`."""

    req_id: str


# Type that contains all possible realtime update message types
UpdateMessage = Union[DownloadedUpdate, CompletedUpdate]
