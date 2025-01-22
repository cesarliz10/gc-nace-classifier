"""Module for NACE code classification."""

import logging
from typing import List

import pandas as pd
from langchain_community.vectorstores import FAISS

from gc_nace_classifier.models import InputColumns as ic
from gc_nace_classifier.models import OutputColumns as oc

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def classify_nace_code(df: pd.DataFrame, nace_vector_store: FAISS) -> pd.DataFrame:
    """Classify each purchase into a NACE code.

    It relies on a similarity score search against a FAISS vector store of NACE codes.
    The supplier name and commodity fields are concatenated

    Parameters
    ----------
    df : pd.DataFrame
        The input purchase data.
    nace_vector_store : FAISS
        The FAISS vector store containing NACE code embeddings.

    Returns
    -------
    pd.DataFrame
        The input DataFrame with an additional column for the classified NACE codes.
    """
    # Combine input features for similarity search
    _c = "combined_text"
    df[_c] = df[ic.supplier_name] + " " + df[ic.commodity]
    # ToDo: refine text combination logic.

    # Define input batch
    input_texts: List[str] = df[_c].tolist()

    # Create input embeddings
    # input_embeddings is a List[embeddings] (with embeddings := List[float])
    input_embeddings = nace_vector_store.embeddings.embed_documents(input_texts)

    # Perform a (batch) similarity search
    results = []
    for purchase in input_embeddings:
        results.append(nace_vector_store.similarity_search_by_vector(purchase, k=1))

    # Extract the best NACE code  match for each input row
    nace_codes = [r[0].metadata[oc.nace_code] for r in results]

    # Add the classified NACE codes to the DataFrame
    df[oc.nace_code] = nace_codes

    # Drop temporal col
    df.drop(columns=[_c], inplace=True)

    return df
