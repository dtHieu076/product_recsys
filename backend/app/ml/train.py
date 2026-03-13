#!/usr/bin/env python3
"""
Train ALS model from DB events data.
Run after populating data.
"""
import asyncio
import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVDpp
from joblib import dump
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import AsyncSessionLocal
from app.entities.event import Event
from sqlalchemy import select

async def load_events_data(db: AsyncSession):
    stmt = select(Event).order_by(Event.event_time)
    result = await db.execute(stmt)
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
            print("No events, skipping training")
            return
        
        reader = Reader(rating_scale=(1,5))
        df = Dataset.load_from_df(pd.DataFrame(data, columns=['user_id', 'product_id', 'rating']), reader)
        trainset = train_test_split(df, test_size=0.2)[0]
        model = SVDpp()
        model.fit(trainset)
        dump(model, 'als_model.pkl')
        print("Model trained and saved to als_model.pkl")

if __name__ == "__main__":
    asyncio.run(train_model())

