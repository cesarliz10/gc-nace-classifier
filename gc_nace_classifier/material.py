"""Module for inference of raw materials."""

from typing import List

import pandas as pd
from mlx_lm import generate

from gc_nace_classifier.models import InputColumns as ic
from gc_nace_classifier.models import OutputColumns as oc
from gc_nace_classifier.rag.llm import model, tokenizer

PROMPT_TEMPLATE = (
    "Commodity description: {commodity_info}.\n\n"
    "Instruction:\n\n"
    "Extract the words corresponding to raw materials from the commodity description provided. "
    "Avoid adjectives or numbers."
    "Provide the result as a pure Python list of the raw material(s) extracted, "
    "without any extra text."
)


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
    # Combine input features for commodity description
    _c = "combined_text"
    df[_c] = df[ic.commodity] + " " + df[ic.sub_commodity]

    # Define input batch
    input_texts: List[str] = df[_c].tolist()

    # Infer materials for batch
    results = []
    for commodity_info in input_texts:
        # Build prompt passed to LLM
        messages = [
            {
                "role": "user",
                "content": PROMPT_TEMPLATE.format(commodity_info=commodity_info),
            }
        ]
        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        # Generate response
        results.append(
            generate(
                model,
                tokenizer,
                prompt=prompt,
                verbose=False,
                max_tokens=512,
            )
        )

    df[oc.raw_materials] = results
    return df
