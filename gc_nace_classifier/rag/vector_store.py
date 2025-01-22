"""Module for vector stores based on NACE code info."""

import logging

import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from gc_nace_classifier.models import OutputColumns as oc

logger = logging.getLogger(__name__)

DEFAULT_EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Path to NACE codes table
NACE_FILE = "data/nace_table.csv"


def build_nace_vector_store(
    embedding_model_name: str = DEFAULT_EMBEDDING_MODEL, save_local: bool = True
) -> FAISS:
    """Build a FAISS vector store for NACE codes.

    It builds the store from a NACE_FILE with a (codes, descriptions) tabular format.

    Parameters
    ----------
    embedding_model_name : str
        Name of HuggingFace model to use for embeddings.
    save_local : bool
        If True, saves locally the vector store.

    Returns
    -------
    FAISS
        The FAISS vector store containing NACE embeddings.
    """
    # Load data source
    nace_table = pd.read_csv(NACE_FILE)
    nace_descriptions = nace_table["description"].tolist()

    # Initialize the embedding model
    embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)

    # Compute embeddings for NACE descriptions
    # embeddings = embedding_model.encode(nace_descriptions, convert_to_numpy=True)

    metadatas = nace_table[[oc.nace_code, oc.description]].to_dict("records")

    # Create FAISS vector store
    vector_store = FAISS.from_texts(
        texts=nace_descriptions,
        embedding=embedding_model,
        metadatas=metadatas,
    )

    # Save the FAISS index locally if the flag is set
    if save_local:
        vector_store.save_local("gc_nace_classifier/rag/faiss_index")

    logger.info("FAISS vector store built with %d entries.", len(nace_descriptions))
    logger.debug(f"FAISS index dimension: {vector_store.index.d}")
    return vector_store
