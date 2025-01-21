"""Module for data preprocessing."""

import pandas as pd

from gc_nace_classifier.models import InputColumns as ic
from gc_nace_classifier.models import OutputColumns as oc


def data_preprocessing(file_path: str) -> pd.DataFrame:
    """
    Validate and Preprocesses the input purchase data.

    The validation consists of reading data with the columns and types specified
    in `InputRow`.

    The preprocessing consists of filling empty values, normalizing and removing white
    spaces from string fields.

    Parameters
    ----------
    file_path : str
        Path to input CSV file.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame with preprocessed data.
    """
    # Read input columns
    input_cols = [ic.commodity, ic.sub_commodity, ic.supplier_name, ic.supplier_country]
    df = pd.read_csv(file_path, usecols=input_cols)

    # Read input columns (with types) specified by the InputRow schema
    if df.empty:
        raise ValueError("The input file is empty.")

    # Fill missing values with an empty string
    df[ic.sub_commodity] = df[ic.sub_commodity].fillna("")

    # Normalize and strip white spaces
    for c in [ic.commodity, ic.sub_commodity, ic.supplier_name, ic.supplier_country]:
        df[c] = df[c].str.lower().str.strip()

    # Create an integer index to each row so they can be identified/traced afterwards.
    df.reset_index(inplace=True)
    df.rename(columns={"index": oc.index}, inplace=True)

    return df
