from typing import Optional, List
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Requirements:
    receiving_temp_low: float
    receiving_temp_high: float


@dataclass_json
@dataclass
class Images:
    source_url: str
    description: str


@dataclass_json
@dataclass
class IngredientsRequests:
    sku: str
    name: str
    vendor_id: str
    category: str
    quality_requirements: Optional[Requirements]
    images: List[Images]
