from uuid import UUID, uuid4
from fastapi import FastAPI,HTTPException
from typing import List
from model import Gender, Role, User, UpdateUser

app  = FastAPI()

db: List[User] = [
    User(id= uuid4(), first_name= "Sol", last_name="Battaglia", gender=Gender.female, roles= [Role.student]),
    User(id= uuid4(), first_name= "JUan", last_name="Wagner", gender=Gender.male, roles= [Role.user, Role.admin])
]

@app.get("/")
async def hello():
    return {"Hello": "World!!"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id":user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db :
        if user.id == user.id:
            db.remove(user)
            return 
    raise HTTPException(status_code = 404, detail=f"User with {user_id} does not exist")


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UpdateUser, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name != None:
                user.first_name = user_update.first_name
            if user_update.last_name != None:
                user.last_name = user_update.last_name
            if user_update.roles != None:
                user.roles = user_update.roles
            return
    raise HTTPException(status_code=404,  detail=f"User with {user_id} does not exist")

