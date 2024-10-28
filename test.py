

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/users")
async def read_users():
    query = users.select()
    all_users = await database.fetch_all(query)
    return {"users": all_users}


@app.post("/users/{user_name}")
async def create_user(user_name: str):
    query = users.select().where(users.c.name == user_name)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this name already exists")
    query = users.insert().values(name=user_name)
    await database.execute(query)
    return {"message": user_name}




