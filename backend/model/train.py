#!/usr/bin/env python3
"""
Train ALS model from DB events data.
Run after populating more data.
"""
import asyncio
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVDpp  # or NMF for ALS-like
from joblib import dump
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database import engine, AsyncSessionLocal
from backend.app.models.event import Event

async def load_events_data(db: AsyncSession):
    # Load events, weight: view=1, cart=3, purchase=5
    result = db.execute(select(Event).order_by(Event.event_time))
    events = result.scalars().all()
    data = []
    for e in events:
        rating = 1 if e.event_type == 'view' else 3 if e.event_type == 'cart' else 5
        data.append((e.user_id, e.product_id, rating))
    return data

async def train_model():
    async with AsyncSessionLocal() as db:
        data = await load_events_data(db)
        if not data:
            print("No events, using dummy")
            return
        
        reader = Reader(rating_scale=(1,5))
        df = Dataset.load_from_df(pd.DataFrame(data, columns=['user_id', 'product_id', 'rating']), reader)
        trainset = train_test_split(df, test_size=0.2)[0]
        model = SVDpp()
        model.fit(trainset)
        dump(model, 'model/als_model.pkl')
        print("Model trained and saved to model/als_model.pkl")

if __name__ == "__main__":
    asyncio.run(train_model())

