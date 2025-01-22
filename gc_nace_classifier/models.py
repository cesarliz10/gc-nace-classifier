"""Data models used by the service."""

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
    # sub_commodity: Optional[str] = None
    sub_commodity: str
    supplier_name: str
    supplier_country: str


# --------------------------
# Data models for Output Data:
# --------------------------


class OutputColumns:
    """Column Registry for output data."""

    index = "purchase_index"
    raw_materials = "raw_materials"
    nace_code = "nace_code"
    description = "description"
