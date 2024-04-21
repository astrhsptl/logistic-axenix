from typing import Optional

from pydantic import BaseModel, Field


class Response(BaseModel):
	detail: str



class NotificationPayload(BaseModel):
    id: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    is_read: Optional[bool] = Field(default=None)
    created_at: Optional[str] = Field(default=None)
    id_warehouse: Optional[str] = Field(default=None)
    id_sale_point: Optional[str] = Field(default=None)