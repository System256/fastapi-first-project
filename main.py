from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
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
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 125, 'amount': 2.12}
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    side: str
    price: float = Field(ge = 0)
    amount: float


@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}


if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)