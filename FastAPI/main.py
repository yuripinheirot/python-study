from fastapi import Cookie, FastAPI, Request, Response
from pydantic import BaseModel
import uuid


class User(BaseModel):
    id: int
    username: str
    password: str


class UserPayload(BaseModel):
    username: str
    password: str


class ChangePasswordPayload(BaseModel):
    old_password: str
    new_password: str


app = FastAPI()


users = [{"username": "yuri", "password": "yuri", "id": "e6043b32"}]


@app.get("/")
def list_users():
    return users


@app.post("/")
def create_user(user: UserPayload):
    new_user = user.model_dump()
    new_user["id"] = str(uuid.uuid1()).split("-")[0]
    users.append(new_user)
    return users[-1]


@app.post("/login")
def login(response: Response, payload: UserPayload):
    response.set_cookie(key="token", value="1234567890")

    user_finded = next(
        (user for user in users if user["username"] == payload.username), None
    )

    if user_finded is None:
        response.status_code = 404
        return {"message": "User not found"}

    return {
        "id": user_finded["id"],
        "username": user_finded["username"],
        "password": user_finded["password"],
    }


@app.post("/change_password")
def change_password(
    request: Request, response: Response, payload: ChangePasswordPayload
):
    token = request.headers.get("Authorization")

    if token is None:
        response.status_code = 401
        return {"message": "Authorization header is required"}

    user_finded = next((user for user in users if user["id"] == token), None)

    if user_finded is None:
        response.status_code = 401
        return {"message": "User not found"}

    if user_finded["password"] != payload.old_password:
        response.status_code = 401
        return {"message": "Old password is incorrect"}

    if payload.new_password == payload.old_password:
        response.status_code = 422
        return {"message": "New password is the same as old password"}

    user_index = users.index(user_finded)

    user_finded["password"] = payload.new_password

    users[user_index] = user_finded

    return {"message": "Password changed"}
