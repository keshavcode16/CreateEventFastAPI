import json
import pathlib
from typing import Any, Dict, List, Union

import requests
from app.api.v1 import crud, models, schemas
from app.api.v1.auth_handler import AuthHandler
from app.api.v1.models import *
from app.config import settings
from app.db import get_db
from app.logs.log_handler import LibLogger
from app.status_messages import response_status
from fastapi import APIRouter, Depends, File, Response, UploadFile, status
from app.utils import verify_password, get_password_hash, create_access_token
from sqlalchemy.orm import Session
from jose import JWTError, jwt


JSONObject: Dict = Dict[str, Any]
JSONArray: List = List[Any]
JSONStructure: Union[List, Dict] = Union[JSONArray, JSONObject]

router: APIRouter = APIRouter()
log: LibLogger = LibLogger()
auth_handler: AuthHandler = AuthHandler()


@router.post("/login",
    summary="Login to User",
    description="Login to User using jwt token.",
)
async def user_login(
    request_data: schemas.LoginSchema,
    response: Response,
    db: Session = Depends(get_db)
):
    """
    Authentication with Jwt Token
    """
    try:
        request_data: Dict = request_data.dict()
        status_val, data = crud.get_user_by_email(
            db=db, 
            model=User,
            user_email=request_data.get('email')
        )
        if status_val:
            password = request_data.get('password')
            if not verify_password(password,data.password):
                response.status_code = status.HTTP_400_BAD_REQUEST
                error_data = {"message":"Email and password combination didn't mached."}
                response.data = error_data
                return error_data
            request_data.update({'password':data.password,"sub": data.email})
            access_token = create_access_token(request_data)
            response.status_code = status.HTTP_200_OK
            return {"message":"User LoggedIn Sucessfully!","access_token":access_token}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message":data}
    except Exception as error:
        log.error(error)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": str(error)}



@router.post("/create",
    summary="Create user",
    description="Create User Account."
)
async def create_user(
    request_data: schemas.UserSchema,
    response: Response,
    db: Session = Depends(get_db)
):
    """
    Endpoint are for use of creating new user.
    """
    try:
        request_data: Dict = request_data.dict()
        status_val, data = crud.get_user_by_email(
            db=db, 
            model=User,
            user_email=request_data.get('email')
        )
        if status_val:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message":"User already exist!"}
        else:
            password = request_data.get('password')
            hashed_password = get_password_hash(password)
            request_data.update({'password':hashed_password})
            is_created, user = crud.save_data(
                payload=request_data, model=User, db=db
            )
            if is_created:
                response.status_code = status.HTTP_201_CREATED
                return user
            else:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"message": user}
    except Exception as error:
        log.error(error)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": str(error)}


@router.get(
    "/",
    summary="All User",
    description="List of all users.",
)
async def all_users(
    response: Response,
    db: Session = Depends(get_db),
    token_payload: Dict = Depends(auth_handler.auth_wrapper),
):
    try:
        status_val, data = crud.get_data(
            db=db,
            model=User
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
    

@router.delete(
    "/{user_id}",
    summary="Delete User",
    description="Delete user by `user_id`.",
)
def delete_user(
    user_id: str,
    response: Response,
    db: Session = Depends(get_db),
    token_payload: Dict = Depends(auth_handler.auth_wrapper),
):
    try:
        status_val, message = crud.delete_data(
            model=User,
            db=db,
            user_id=user_id
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

