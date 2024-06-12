from typing import Any, Dict, List, Union
from app.api.v1 import crud, models, schemas
from app.api.v1.models import *
from app.db import get_db
from app.logs.log_handler import LibLogger
from app.status_messages import response_status
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
import traceback


JSONObject: Dict = Dict[str, Any]
JSONArray: List = List[Any]
JSONStructure: Union[List, Dict] = Union[JSONArray, JSONObject]

router: APIRouter = APIRouter()
log: LibLogger = LibLogger()




@router.get(
    "/",
    summary="Get Events",
    description="List of all events.",
)
async def all_events(
    response: Response,
    db: Session = Depends(get_db)
):
    try:
        status_val, data = crud.get_data(
            db=db,
            model=Event
        )
        if status_val:
            response.status_code = status.HTTP_200_OK
            return data
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": data}
    except Exception as error:
        log.error(error)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": str(error)}
    
    


@router.post("/",
    summary="Create Event",
    description="Create New Event."
)
async def create_event(
    request_data: schemas.EventSchema,
    response: Response,
    db: Session = Depends(get_db)
):
    """
    Endpoint are for use of creating new event.
    """
    try:
        request_data: Dict = request_data.dict()
        is_created, event = crud.save_event_data(
            payload=request_data, model=Event, db=db
        )
        if is_created:
            response.status_code = status.HTTP_201_CREATED
            return event
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": event}
    except Exception as error:
        log.error(error)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": str(error)}


@router.get(
    "/{id}",
    summary="Get Event Detail API",
    description="Get Event detail by `id`.",
)
def get_event_detail(
    id: str,
    response: Response,
    db: Session = Depends(get_db)
):
    try:
        status_val, event_data = crud.get_data(
            model=Event,
            db=db,
            pk_uuid=id
        )
        if status_val:
            response.status_code = status.HTTP_200_OK
            return {"event": event_data}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": event_data}
    except Exception as error:
        log.error(error)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": str(error)}



@router.post(
    "/{id}/book",
    summary="Book Ticket for an Event",
    description="Book Ticket for an Event by event id and number of ticket"
)
async def book_event(
    id: str,
    request_data: schemas.CreateBookingSchema,
    response: Response,
    db: Session = Depends(get_db)
):
    """
    Endpoint are for use of booking an event.
    """
    try:
        request_data: Dict = request_data.dict()
        request_data.update({'event_id':id})
        status_val, event = crud.get_data(
            model=Event,
            db=db,
            pk_uuid=id
        )
        if status_val:
            num_tickets = request_data.get('num_tickets', 0)
            if event.available_tickets < num_tickets:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"message":f"Tickets are not available for this event {id}"}
            
            is_created, booking = crud.book_event(
                payload=request_data, event_model_obj=event, model=Booking, num_tickets=num_tickets, db=db
            )
            if is_created:
                response.status_code = status.HTTP_201_CREATED
                return booking
            else:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"message": booking}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message":event}
    except Exception as error:
        log.error(error)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": str(error)}



@router.delete(
    "/{id}",
    summary="Delete Event",
    description="Delete event by `id`.",
)
def delete_event(
    id: str,
    response: Response,
    db: Session = Depends(get_db)
):
    try:
        status_val, message = crud.delete_data(
            model=Event,
            db=db,
            pk_uuid=id
        )
        if status_val:
            response.status_code = status.HTTP_200_OK
            return {"message": message}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": message}
    except Exception as error:
        log.error(error)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": str(error)}
