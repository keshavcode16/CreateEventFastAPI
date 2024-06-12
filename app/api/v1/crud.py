import os
from typing import Any, Dict, List, Tuple, Union
from app.api.v1.models import *
from app.api.v1.services import get_maps_url 
from app.logs.log_handler import LibLogger
from app.status_messages import response_status
from sqlalchemy.orm import Session
import traceback

log: LibLogger = LibLogger()


def get_user_by_email(db: Session, model, user_email: str):
    try:
        data: Union[model, None] = db.query(model).filter_by(email=user_email).first()
        if data:
            return True, data
        else:
            return False, response_status.RECORD_NOT_EXIST
    except Exception as error:
        log.error(error)
        return False, str(error)

def save_event_data(payload: Dict, model, db: Session):
    try:
        location = payload.get('location', None)
        map_url = get_maps_url(location)
        payload.update({'map_url':map_url})
        data = model(**payload)
        db.add(data)
        db.commit()
        db.refresh(data)
        return True, data
    except Exception as error:
        traceback.print_exc()
        log.error(error)
        db.rollback()
        return False, str(error)



def save_data(payload: Dict, model, db: Session):
    try:
        data = model(**payload)
        db.add(data)
        db.commit()
        db.refresh(data)
        return True, data
    except Exception as error:
        traceback.print_exc()
        log.error(error)
        db.rollback()
        return False, str(error)


def get_data(db: Session, model, **kwargs):
    try:
        data: List = db.query(model).all()
        pk_uuid: Union[str, None] = kwargs.get("pk_uuid")
        if data and pk_uuid is None:
            return True, data
        elif pk_uuid:
            data: Union[model, None] = db.query(model).filter_by(id=pk_uuid).first()
            if data:
                return True, data
        return False, response_status.RECORD_NOT_EXIST
    except Exception as error:
        log.error(error)
        return False, str(error)



def delete_data(model, db: Session, **kwargs: Dict):
    try:
        pk_uuid: Union[str, None] = kwargs.get("pk_uuid")
        if pk_uuid:
            data: Union[model, None] = db.query(model).filter_by(id=pk_uuid).first()
            if data:
                db.delete(data)
                db.commit()
                return True, response_status.DELETED
            else:
                return False, response_status.DATA_NOT_FOUND
        else:
            return False, response_status.DATA_NOT_FOUND
    except Exception as error:
        db.rollback()
        log.error(error)
        return False, str(error)
    


def book_event(payload: Dict, event_model_obj, model, num_tickets, db: Session):
    try:
        event_model_obj.available_tickets -= num_tickets
        booking_model = model(**payload)
        db.add(booking_model)
        db.commit()
        db.refresh(booking_model)
        db.refresh(event_model_obj)
        return True, "Booking created successfully"
    except Exception as error:
        traceback.print_exc()
        log.error(error)
        db.rollback()
        return False, str(error)