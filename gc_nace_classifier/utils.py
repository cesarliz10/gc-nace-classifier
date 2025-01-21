"""Utilities for nace classifier."""

import tempfile
from typing import BinaryIO

from fastapi import HTTPException, UploadFile


def to_tmp_file(file: BinaryIO) -> str:
    """
    Store a binary file to a temporal csv file.

    Parameters
    ----------
    file : BinaryIO
        The binary file-like object to save.

    Returns
    -------
    str
        The path to the temporary file.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
        temp_file.write(file.read())
        return temp_file.name


def validate_file(file: UploadFile) -> None:
    """
    Validate that uploaded file is a CSV.

    Parameters
    ----------
    file : UploadFile
        The uploaded file to validate.
    """
    if not file.filename or not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400, detail="Invalid file format. Only CSV is supported."
        )
