import logging
import asyncio
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, FileResponse

from .repository import indexes


router = APIRouter()
lock = asyncio.Lock()


@router.get("/{directory}/directory.json")
@router.get("/{directory}")
async def directory_request(directory):
    """
    Method for obtaining indices
    Args:
        directory: Repository name

    Returns:
        Indices in json
    """
    if directory not in indexes:
        return JSONResponse(f"{directory} not found!", status_code=404)
    return indexes.get(directory).index


@router.get("/{directory}/{branch}")
async def repository_branch_request(directory, branch):
    """
    A method for retrieving the list of files from a specific branch
    Made for support of `ufbt update --index-url {base_url}/firmware --branch {branch}`
    Args:
        directory: Repository name
        branch: Branch name

    Returns:
        HTML links in format that ufbt understands
    """
    if directory not in indexes:
        return JSONResponse(f"{directory} not found!", status_code=404)
    index = indexes.get(directory)
    if len(index.index["channels"]) == 0:
        return JSONResponse("No channels found!", status_code=404)
    try:
        branch_files = index.get_branch_file_names(branch)
        response = "\n".join(f'<a href="{file}"></a>' for file in branch_files)
        return HTMLResponse(
            response,
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(str(e), status_code=404)

@router.get(
    "/{directory}/{channel}/{target}/{file_type}",
    response_class=RedirectResponse,
    status_code=302,
)
async def latest_request(directory, channel, target, file_type):
    """
    A method for retrieving a file from the repository
    of a specific version
    Args:
        directory: Repository name
        channel: Channel type (release, dev)
        target: Operating System (linux, mac, win)
        file_type: File Type

    Returns:
        Artifact file
    """
    if directory not in indexes:
        return JSONResponse(f"{directory} not found!", status_code=404)
    index = indexes.get(directory)
    if len(index.index["channels"]) == 0:
        return JSONResponse("No channels found!", status_code=404)
    try:
        return index.get_file_from_latest_version(channel, target, file_type)
    except Exception as e:
        return JSONResponse(str(e), status_code=404)


@router.get("/{directory}/{channel}/{file_name}")
async def file_request(directory, channel, file_name):
    """
    A method for retrieving a file from the repository
    of a specific version
    Args:
        directory: Repository name
        channel: Channel type (release, dev)
        file_name: File Name

    Returns:
        Artifact file
    """
    if directory not in indexes:
        return JSONResponse(f"{directory} not found!", status_code=404)
    index = indexes.get(directory)
    if len(index.index["channels"]) == 0:
        return JSONResponse("No channels found!", status_code=404)
    try:
        return FileResponse(
            index.get_file_path(channel, file_name),
            media_type="application/octet-stream",
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(str(e), status_code=404)


@router.get("/{directory}/reindex")
async def reindex_request(directory):
    """
    Method for starting reindexing
    Args:
        directory: Repository name

    Returns:
        Reindex status
    """
    if directory not in indexes:
        return JSONResponse(f"{directory} not found!", status_code=404)
    async with lock:
        try:
            indexes.get(directory).reindex()
            return JSONResponse("Reindexing is done!")
        except Exception as e:
            logging.exception(e)
            return JSONResponse("Reindexing is failed!", status_code=500)
