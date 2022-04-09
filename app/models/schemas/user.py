from app.models.domain import (
                                base as _base,
                                user as _user_domain)

            
class UserCreate(
    _user_domain.UserHten,
    _user_domain.UserMk,
    _user_domain.UserTk
):
    pass


class UserDetail(
    _base.UserId,
    _user_domain.UserHten,
    _user_domain.UserMk,
    _user_domain.UserTk
):
    pass

    class Config:
        orm_mode = True


class UserUpdate(
    _base.UserId,
    _user_domain.UserHten,
    _user_domain.UserMk,
    _user_domain.UserTk
):
    pass


class UserToken(
    _base.UserId,
    _user_domain.UserHten,
):
    pass


class UserLogin(    
    _user_domain.UserMk,
    _user_domain.UserTk
):
    pass