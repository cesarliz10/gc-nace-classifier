"""Module for API definition."""

from typing import Dict

from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI()


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


@app.post("/infer-raw-materials")
async def infer_raw_materials(file: UploadFile = File(...)) -> Dict:
    """
    Endpoint to infer the raw materials for each purchase.

    Parameters
    ----------
    file : UploadFile
        A CSV input file with a purchase description per row.

    Returns
    -------
    Dict
        A dictionary with the original data and inferred raw materials.
    """
    validate_file(file)

    # Placeholder response to be replaced in later steps
    return {"message": "Raw materials classification logic not yet implemented."}


@app.post("/classify-nace")
async def classify_nace(file: UploadFile = File(...)) -> Dict:
    """
    Endpoint to classify a NACE code for each purchase.

    Parameters
    ----------
    file : UploadFile
        A CSV input file with a purchase description per row.

    Returns
    -------
    Dict
        A dictionary with the original data and inferred NACE codes.
    """
    validate_file(file)

    # Placeholder response to be replaced in later steps
    return {"message": "NACE code classification logic not yet implemented."}
