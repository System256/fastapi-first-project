from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title = 'Trading App'
)


fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Roman'},
    {'id': 2, 'role': 'investor', 'name': 'Bob'},
    {'id': 3, 'role': 'trader', 'name': 'Anna'},
]

@app.get('/users/{user_id}')
def get_user(user_id):
    return user_id


if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)