from datetime import datetime, timedelta, timezone
from fastapi import Cookie, Depends, FastAPI, HTTPException, Request, Response
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt
import uuid

users = [
    {
        "username": "admin",
        "password": "$2b$12$twEcV0huWKR8kqP1NZglyu2lhHyJTpwk8mcbOMtvhXFJ4ewGYi2ZS",
        "id": "e6043b32",
    }
]


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401, detail="Could not validate credentials"
    )


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


@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request path: {request.url.path}")
    response = await call_next(request)
    print(f"Response status: {response.status_code}")
    return response


@app.get("/")
def list_users():
    return users


@app.post("/")
def create_user(user: UserPayload):
    new_user = user.model_dump()
    new_user["id"] = str(uuid.uuid1()).split("-")[0]
    new_user["password"] = get_password_hash(new_user["password"])
    users.append(new_user)
    return users[-1]


@app.post("/login")
def login(response: Response, payload: UserPayload):
    user_finded = next(
        (user for user in users if user["username"] == payload.username), None
    )

    if user_finded is None:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(payload.password, user_finded["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")

    response.set_cookie(key="token", value=user_finded["id"])

    token = create_access_token(data={"sub": user_finded["id"]})

    return {"access_token": token}


def query_param(my_param: str = None, limit: int = 10):
    return {"my_param": my_param, "limit": limit}


@app.get("/search")
def search(params: dict = Depends(query_param)):
    return params


@app.post("/change_password")
def change_password(
    request: Request, response: Response, payload: ChangePasswordPayload
):
    token = request.headers.get("Authorization")

    if token is None:
        raise HTTPException(status_code=401, detail="Authorization header is required")

    user_finded = next((user for user in users if user["id"] == token), None)

    if user_finded is None:
        raise HTTPException(status_code=401, detail="User not found")

    if user_finded["password"] != payload.old_password:
        raise HTTPException(status_code=401, detail="Old password is incorrect")

    if payload.new_password == payload.old_password:
        raise HTTPException(
            status_code=422, detail="New password is the same as old password"
        )

    user_index = users.index(user_finded)

    user_finded["password"] = payload.new_password

    users[user_index] = user_finded

    return {"message": "Password changed"}
