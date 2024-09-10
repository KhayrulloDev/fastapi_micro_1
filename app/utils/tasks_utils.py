import httpx
from fastapi import HTTPException


async def fetch_channels():
    async with httpx.AsyncClient() as client:
         try:
            response = await client.get('http://192.168.100.133:8001/list-channels')
            response.raise_for_status()
            return response.json()
         except Exception as e:
             raise HTTPException(status_code=e.response.status_code, detail="Error fetching tasks")