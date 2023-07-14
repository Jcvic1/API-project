
from typing import List
import schemas
import models
from crud import CRUD
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from database import get_db
from typing_extensions import Annotated
from authentication import get_current_active_user

router = APIRouter()




note_crud = CRUD(item_class=models.Note, search_filter_option=models.Note.title)





@router.post('/users/me/notes/', response_model=schemas.Note)
async def create_note(current_user: Annotated[schemas.User, Depends(get_current_active_user)], item_schema:schemas.NoteCreate, db: Session = Depends(get_db)):
    new_note = note_crud.create_user_item(db=db, item_schema=item_schema, current_user=current_user)
    return new_note

@router.get('/users/me/notes/', response_model=List[schemas.Note])
async def read_notes(current_user: Annotated[schemas.User, Depends(get_current_active_user)], db: Session = Depends(get_db),  limit: int = 10, page: int = 1, search: str = ''):
    notes = note_crud.read_user_items(db=db, limit=limit, page=page, search=search)
    return notes

@router.get('/users/me/notes/', response_model=schemas.Note)
async def read_note(current_user: Annotated[schemas.User, Depends(get_current_active_user)], db: Session = Depends(get_db)):
    note = note_crud.read_user_item(db=db, item_id=note_id)
    return note


@router.patch('/users/me/notes/', response_model=schemas.Note)
async def update_note(current_user: Annotated[schemas.User, Depends(get_current_active_user)], item_schema:schemas.NoteUpdate, db: Session = Depends(get_db)):
    updated_note = note_crud.update_user_item(db=db, item_schema=item_schema, item_id=note_id)
    return updated_note


@router.delete('/users/me/notes/')
async def delete_note(current_user: Annotated[schemas.User, Depends(get_current_active_user)], db: Session = Depends(get_db)):
    return note_crud.delete_user_item(db=db, item_id=note_id)
