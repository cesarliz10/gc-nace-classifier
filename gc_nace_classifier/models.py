"""Data models used by the service."""

from typing import List, Optional

from pydantic import BaseModel

# --------------------------
# Data models for Input Data:
# --------------------------


class InputColumns:
    """Column Registry for input data."""

    commodity = "Commodity"
    sub_commodity = "Sub-Commodity"
    supplier_name = "Supplier Name"
    supplier_country = "Supplier Country"


class InputRow(BaseModel):
    """Single row of purchase data."""

    commodity: str
    sub_commodity: Optional[str] = None
    supplier_name: str
    supplier_country: str


class InputData(BaseModel):
    """Validated input data for an input batch request."""

    rows: List[InputRow]


# --------------------------
# Data models for Output Data:
# --------------------------


class OutputColumns:
    """Column Registry for output data."""

    index = "index"
    raw_materials = "raw_materials"
    nace_code = "nace_code"


class RawMaterialsOutputRow(BaseModel):
    """Raw materials inferred for a single purchase."""

    index: int
    raw_materials: List[str]


class RawMaterialsOutputData(BaseModel):
    """Output data for raw materials batch inference."""

    rows: List[RawMaterialsOutputRow]


class NACEOutputRow(BaseModel):
    """NACE classification for a single purchase."""

    index: int
    nace_code: str


class NACEOutputData(BaseModel):
    """Output data for NACE batch classification."""

    rows: List[NACEOutputRow]
