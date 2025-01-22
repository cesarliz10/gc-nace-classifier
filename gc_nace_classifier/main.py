"""Module for API definition."""

from typing import Dict

from fastapi import FastAPI, File, UploadFile

from gc_nace_classifier.classify import classify_nace_code
from gc_nace_classifier.material import infer_raw_materials
from gc_nace_classifier.models import InputColumns as ic
from gc_nace_classifier.models import OutputColumns as oc
from gc_nace_classifier.preprocess import data_preprocessing
from gc_nace_classifier.rag.vector_store import build_nace_vector_store
from gc_nace_classifier.utils import to_tmp_file, validate_file

# Create fast-api instance
app = FastAPI()

# Build the vector store for NACE codes
nace_vector_store = build_nace_vector_store(save_local=True)


@app.post("/classify-nace")
async def classify_nace(file: UploadFile = File(...)) -> Dict:
    """
    Endpoint to classify a NACE code for each purchase.

    Parameters
    ----------
    file : UploadFile
        A CSV file containing purchase data.

    Returns
    -------
    Dict
        A JSON response containing the index + NACE code results per purchase.
    """
    # Validate input and save to tmp file
    validate_file(file)
    tmp_path = to_tmp_file(file.file)
    # Preprocess data
    df = data_preprocessing(tmp_path)
    # Classification for NACE code
    nace_df = classify_nace_code(df, nace_vector_store)
    # Return dictionary result
    response = nace_df[
        [oc.index, oc.nace_code, oc.description, ic.supplier_name, ic.commodity]
    ].to_dict(orient="records")
    return {"rows": response}


@app.post("/raw-materials")
async def raw_materials(file: UploadFile = File(...)) -> Dict:
    """
    Endpoint to infer raw materials for each purchase (row) in the CSV.

    Parameters
    ----------
    file : UploadFile
        A CSV file containing purchase data.

    Returns
    -------
    Dict
        A JSON response containing the index + raw materials per purchase.
    """
    # Validate input and save to tmp file
    validate_file(file)
    tmp_path = to_tmp_file(file.file)
    # Preprocess data
    df = data_preprocessing(tmp_path)
    # Infer raw materials
    materials_df = infer_raw_materials(df)
    # Return dictionary result
    response = materials_df[
        [oc.index, ic.commodity, ic.sub_commodity, oc.raw_materials]
    ].to_dict(orient="records")
    return {"rows": response}
