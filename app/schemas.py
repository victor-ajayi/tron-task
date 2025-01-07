from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class GetInfoIn(BaseModel):
    address: str


class GetInfoOut(BaseModel):
    model_config = ConfigDict(extra="ignore")

    account_name: str
    address: str
    type: str
    balance: float
    net_window_size: float
    account_resource: dict


class Request(BaseModel):
    id: int
    account_name: str
    address: str
    created_at: datetime


class GetRequestsOut(BaseModel):
    total: int
    next: Optional[str] = None
    previous: Optional[str] = None
    data: list[Request]
