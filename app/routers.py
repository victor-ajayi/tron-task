from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session
from tronpy import Tron
from tronpy.providers import HTTPProvider

from app import models
from app.config import settings
from app.database import get_db
from app.schemas import GetInfoIn, GetInfoOut, GetRequestsOut

client = Tron(HTTPProvider(api_key=settings.TRON_PRO_API_KEY))

router = APIRouter(prefix="/wallets", tags=["Wallet"])


@router.post("/")
def get_info(
    data: GetInfoIn, session: Annotated[Session, Depends(get_db)]
) -> GetInfoOut:
    try:
        account = client.get_account(data.address)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    data = dict(**data.model_dump())
    data.update({"account_name": account["account_name"]})

    try:
        session.add(models.Request(**data))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    session.commit()

    response = GetInfoOut(**account)
    return response


@router.get("/")
def get_all_requests(
    session: Annotated[Session, Depends(get_db)], limit: int = 10, offset: int = 0
) -> GetRequestsOut:
    total = session.execute(
        select(func.count("*")).select_from(models.Request)
    ).scalar_one()
    query = select(models.Request).limit(limit).offset(offset)
    data = [d.__dict__ for d in session.execute(query).scalars().all()]

    response = GetRequestsOut(data=data, total=total)
    return response
