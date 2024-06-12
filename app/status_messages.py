class ResponseStatuses(object):
    LOGOUT: str = "User Successfully Logout"
    NOT_LOGIN: str = "User is not logged in"
    UPDATED: str = "Data updated"
    USER_NOT_EXIST: str = "User doesn't exists"
    DATA_NOT_FOUND: str = "Data Not Found"
    DATA_FOUND: str = "Data Found"
    INVALID_TOKEN: str = "Invalid Token"
    DELETED: str = "Record Deleted"
    NOT_AUTHORIZED: str = "You don't have permissions"
    NOT_CHANGE_CURRENT: str = "You can't change your own status/role"
    VALID_ACCESS_TOKEN: str = "Access token is valid"
    INVALID_ACCESS_TOKEN: str = "Unauthorized / Invalid Token"
    ACCESS_TOKEN_EXPIRED: str = "Token Expired"
    REFRESH_TOKEN_EXPIRED: str = "Refresh Token Expired"
    INVALID_REFRESH_TOKEN: str = "Invalid Refresh Token"
    GRANT_ACCESS_TO_ONBOARDING: str = "Permissions granted to user"
    ONBOARDING_USER_AUTHRIZED: str = "Permissions already granted to this user"
    TOKEN_EXPIRED: str = "Token Expired"
    INVALID_ID: str = "Invalid ID"
    FILE_UPLOADED: str = "File Uploaded"
    ALL_FILE_UPLOADED: str = "All files are uploaded"
    RECORD_NOT_EXIST: str = "Record not found"


response_status: ResponseStatuses = ResponseStatuses()