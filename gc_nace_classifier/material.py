"""Module for inference of raw materials."""

from typing import List

import pandas as pd

from gc_nace_classifier.models import InputColumns as ic
from gc_nace_classifier.models import OutputColumns as oc


def infer_raw_materials(df: pd.DataFrame) -> pd.DataFrame:
    """Infer raw materials for each purchase.

    Parameters
    ----------
    df : pd.DataFrame
        Preprocessed purchase data.

    Returns
    -------
    pd.DataFrame
        The input DataFrame with an additional column for raw materials.
    """
    _ = None

    def _infer(row: pd.Series) -> List[str]:
        """Infer raw material dummy."""
        materials = []
        commodity = row[ic.commodity]
        sub_commodity = row[ic.sub_commodity]

        # Example rule-based classification
        if "steel" in commodity or "steel" in sub_commodity:
            materials.append("steel")
        if "wood" in commodity or "wood" in sub_commodity:
            materials.append("wood")
        if "fabric" in commodity or "fabric" in sub_commodity:
            materials.append("fabric")
        if "plastic" in commodity or "plastic" in sub_commodity:
            materials.append("plastic")

        return materials

    # Apply the classification logic
    df[oc.raw_materials] = df.apply(_infer, axis=1)
    return df
