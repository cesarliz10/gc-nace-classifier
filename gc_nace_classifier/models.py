from pydantic import BaseModel
from typing import List

class InputRow(BaseModel):
    description: str
    subcommodities: List[str]

class InputData(BaseModel):
    rows: List[InputRow]

class OutputRow(BaseModel):
    raw_materials: List[str]
    nace_code: str

class OutputData(BaseModel):
    rows: List[OutputRow]