from typing import Optional, Type
from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException





class CRUD :
    def __init__(self, item_class, search_filter_option: Optional[type] = None):
        self.item_class = item_class
        self.search_filter_option = search_filter_option


    def create_user_item(self, db: Session, current_user, item_schema: Type):
        db_item = self.item_class(**item_schema.dict(), owner_id=current_user.id)
        db_item.owner = current_user
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def read_user_item(self, db: Session, item_id: int):
        item_query = db.query(self.item_class).filter(self.item_class.id == item_id)
        db_item = item_query.first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item

    def read_user_items(self, db: Session, limit: int = 20, page: int = 1, search: Optional[str] = None):
        skip = (page - 1) * limit
        return db.query(self.item_class).filter(self.search_filter_option.contains(search)).limit(limit).offset(skip).all()

    def update_user_item(self, db: Session, item_schema: Type, item_id: int):
        item_query = db.query(self.item_class).filter(self.item_class.id == item_id)
        db_item = item_query.first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        update_data = item_schema.dict(exclude_unset=True)
        item_query.filter(self.item_class.id == item_id).update(update_data,synchronize_session=False)
        db.commit()
        db.refresh(db_item)
        return db_item

    def delete_user_item(self, db: Session, item_id: int):
        item_query = db.query(self.item_class).filter(self.item_class.id == item_id)
        db_item = item_query.first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        item_query.delete(synchronize_session=False)
        db.commit()


