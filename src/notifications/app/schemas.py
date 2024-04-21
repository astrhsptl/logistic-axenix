from pydantic import BaseModel


class Response(BaseModel):
	detail: str



class NotificationPayload(BaseModel):
    id: str | None
    name: str | None
    description: str | None
    is_read: bool
    created_at: str | None
    id_warehouse: str | None
    id_sale_point: str | None