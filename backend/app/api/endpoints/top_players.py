# app/api/endpoints/top_players.py

from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

@router.get("/top-players")
def get_top_players():
    try:
        lichess_api_url = "https://lichess.org/api/player/top/50/classical"

        # Debugging statement
        print(f"Requesting data from {lichess_api_url}")

        response = requests.get(lichess_api_url)

       

        if response.status_code == 200:
            # Handle HTML response
            if "text/html" in response.headers.get("content-type", "").lower():
                raise HTTPException(status_code=500, detail="Received HTML response instead of JSON from Lichess API")
            
            try:
                # Attempt to parse the response as JSON
                top_players_data = response.json()
                
                if 'users' in top_players_data:
                    top_players = top_players_data['users'][:50]
                    return top_players
                else:
                    raise HTTPException(status_code=500, detail="Unexpected JSON response format from Lichess API")
            except Exception as json_error:
                raise HTTPException(status_code=500, detail="Failed to parse JSON response from Lichess API")
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to retrieve top players from Lichess API")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
