from fastapi import FastAPI, Form


app = FastAPI()

# BEGIN (write your solution here)
@app.post("/login")
async def handle_form(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password, "status": "Login successful"}
# END
