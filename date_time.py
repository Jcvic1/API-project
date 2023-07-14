from datetime import datetime
import schemas
from fastapi import Depends, APIRouter
from typing_extensions import Annotated
from authentication import verify_user


router = APIRouter()


@router.get('/date/',  response_model=schemas.DateTime)
async def date(current_user: Annotated[schemas.DateTime, Depends(verify_user)]):

    current_date = datetime.now()

    day = current_date.strftime("%d")
    month = current_date.strftime("%B")
    year = current_date.strftime("%Y")
    time = current_date.strftime("%H:%M")
    return{
    "Day": day,
    "Month": month,
    "Year": year,
    "Time": time
    }