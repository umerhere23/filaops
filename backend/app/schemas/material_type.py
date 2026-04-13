"""Material type schemas used by admin CRUD flows."""
from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MaterialTypeCreate(BaseModel):
    """Create a material type."""
    code: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., min_length=1, max_length=100)
    base_material: str = Field(..., min_length=1, max_length=20)
    process_type: str = Field(default="FDM", min_length=1, max_length=20)
    density: Decimal = Field(..., gt=0)
    volumetric_flow_limit: Optional[Decimal] = Field(default=None, gt=0)
    nozzle_temp_min: Optional[int] = Field(default=None, ge=0)
    nozzle_temp_max: Optional[int] = Field(default=None, ge=0)
    bed_temp_min: Optional[int] = Field(default=None, ge=0)
    bed_temp_max: Optional[int] = Field(default=None, ge=0)
    requires_enclosure: bool = False
    filament_diameter: Decimal = Field(default=Decimal("1.75"), gt=0)
    base_price_per_kg: Decimal = Field(..., ge=0)
    price_multiplier: Decimal = Field(default=Decimal("1.0"), ge=0)
    description: Optional[str] = None
    strength_rating: Optional[int] = Field(default=None, ge=1, le=10)
    is_customer_visible: bool = True
    display_order: int = Field(default=100, ge=0)
    active: bool = True


class MaterialTypeUpdate(BaseModel):
    """Update a material type."""
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    base_material: Optional[str] = Field(default=None, min_length=1, max_length=20)
    process_type: Optional[str] = Field(default=None, min_length=1, max_length=20)
    density: Optional[Decimal] = Field(default=None, gt=0)
    volumetric_flow_limit: Optional[Decimal] = Field(default=None, gt=0)
    nozzle_temp_min: Optional[int] = Field(default=None, ge=0)
    nozzle_temp_max: Optional[int] = Field(default=None, ge=0)
    bed_temp_min: Optional[int] = Field(default=None, ge=0)
    bed_temp_max: Optional[int] = Field(default=None, ge=0)
    requires_enclosure: Optional[bool] = None
    filament_diameter: Optional[Decimal] = Field(default=None, gt=0)
    base_price_per_kg: Optional[Decimal] = Field(default=None, ge=0)
    price_multiplier: Optional[Decimal] = Field(default=None, ge=0)
    description: Optional[str] = None
    strength_rating: Optional[int] = Field(default=None, ge=1, le=10)
    is_customer_visible: Optional[bool] = None
    display_order: Optional[int] = Field(default=None, ge=0)
    active: Optional[bool] = None


class MaterialTypeResponse(BaseModel):
    """Material type API response."""
    id: int
    code: str
    name: str
    base_material: str
    process_type: str
    density: Decimal
    volumetric_flow_limit: Optional[Decimal] = None
    nozzle_temp_min: Optional[int] = None
    nozzle_temp_max: Optional[int] = None
    bed_temp_min: Optional[int] = None
    bed_temp_max: Optional[int] = None
    requires_enclosure: bool
    filament_diameter: Decimal
    base_price_per_kg: Decimal
    price_multiplier: Decimal
    description: Optional[str] = None
    strength_rating: Optional[int] = None
    is_customer_visible: bool
    display_order: int
    active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
