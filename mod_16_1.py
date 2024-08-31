from fastapi import FastAPI
import uvicorn


app = FastAPI(tags = ["dev"])

@app.get("/")
def get_main_page():
    return "Главная страница"

@app.get("/user/admin")
def get_admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
def get_user_id(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
def get_username_and_age(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


if __name__ == "__main__":
    uvicorn.run("mod_16_1:app", reload=True)