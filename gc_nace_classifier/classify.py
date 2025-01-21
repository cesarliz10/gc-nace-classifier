"""Module for NACE code classification."""

import pandas as pd

from gc_nace_classifier.models import InputColumns as ic
from gc_nace_classifier.models import OutputColumns as oc


def classify_nace_code(df: pd.DataFrame) -> pd.DataFrame:
    """Classifies each purchase into a NACE code.

    Parameters
    ----------
    df : pd.DataFrame
        Preprocessed purchase data.

    Returns
    -------
    pd.DataFrame
        The input DataFrame with an additional column for NACE codes.
    """
    # Example mapping of commodities to NACE codes
    nace_mapping = {
        "recyclable waste": "38.21",
        "work clothes": "14.12",
        "gloves": "14.19",
        "table trolleys": "31.01",
    }

    def infer_nace_code(row: pd.Series) -> str:
        commodity = row[ic.commodity]
        for keyword, code in nace_mapping.items():
            if keyword in commodity:
                return code
        return "00.00"  # Default NACE code for unknown items

    # Apply the classification logic
    df[oc.nace_code] = df.apply(infer_nace_code, axis=1)
    return df
