import io
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from typing import List

import requests

router = APIRouter()

def get_top_players():
    url = "https://lichess.org/api/player/top/50/classical"
    response = requests.get(url)
    
    try:
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from Lichess API: {str(e)}")

@router.get("/players/rating-history-csv")
async def get_rating_history_csv(
    top_players: List[str] = Depends(get_top_players)
):
    # Create CSV content as bytes
    csv_content = io.BytesIO()
    csv_content.write(bytes(f"username\n" + "\n".join(top_players), "utf-8"))
    
    return StreamingResponse(
        content=csv_content.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=rating_history.csv"},
    )
