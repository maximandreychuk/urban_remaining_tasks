from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn


app = FastAPI(tags = ["dev"])

@app.get("/")
def get_main_page():
    return "Главная страница"

@app.get("/user/admin")
def get_admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
def get_user_id(user_id: int = Path(
    min_length=1,
    max_length=100,
    description="Enter User ID",
    examples=["2"], # DeprecationWarning: `example` has been deprecated, please use `examples` instead
)):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
def get_username_and_age(
        username: Annotated[
            str, Path(
                min_length=5,
                max_length=20,
                description="Enter username",
                examples=["UrbanUser"],
)],
        age: Annotated[
            int, Path(
                ge=18,
                le=120,
                description="Enter age",
                examples=[24],
)]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


if __name__ == "__main__":
    uvicorn.run("mod_16_2:app", reload=True)