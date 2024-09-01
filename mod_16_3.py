from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn


app = FastAPI(tags = ["crud"])

users = {1: "Имя: Example, возраст: 18", 2: "fsv" }

@app.get("/")
async def get_all_messages() -> dict:
    return users

@app.get("/message/{user_id}")
async def get_message(
        user_id: Annotated[
            int, Path(
                ge=1,
                le=100,
            )
        ],
) -> dict:
    return {user_id: users[user_id]}

@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[
            str, Path(
                min_length=5,
                max_length=20,
                description="Enter username",
                examples=["UrbanUser"],
            )
        ],
        age: Annotated[
            int, Path(
                ge=18,
                le=120,
                description="Enter age",
                examples=[24],
            )
        ]
) -> str:
    new_id: int = max(users)+1
    users[new_id]=f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[
            int, Path(
                ge=1,
                le=100,
            )
        ],
        username: Annotated[
            str, Path(
                min_length=5,
                max_length=20,
                description="Enter username",
                examples=["UrbanUser"],
            )
        ],
        age: Annotated[
            int, Path(
                ge=18,
                le=120,
                description="Enter age",
                examples=[24],
            )
        ],
) -> str:
    users[user_id]=f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[
            int, Path(
                ge=1,
                le=100,
            )
        ],
) -> None:
    users.pop(user_id)




if __name__ == "__main__":
    uvicorn.run("mod_16_3:app", reload=True, port=8000)