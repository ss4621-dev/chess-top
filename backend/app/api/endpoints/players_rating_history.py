# app/api/endpoints/player_rating_history.py

from fastapi import APIRouter, HTTPException, Path
import requests

router = APIRouter()

@router.get("/player/{username}/rating-history")
def get_player_rating_history(username: str = Path(..., title="The username of the player")):
    try:
        lichess_api_url = f"https://lichess.org/api/user/{username}/rating-history"

        response = requests.get(lichess_api_url)

        if response.status_code == 200:
            # Handle HTML response
            if "text/html" in response.headers.get("content-type", "").lower():
                raise HTTPException(status_code=500, detail="Received HTML response instead of JSON from Lichess API")

            try:
                # Attempt to parse the response as JSON
                rating_history = response.json()
                return rating_history
            except Exception as json_error:
                # Log the JSON parsing error
                print(f"Error parsing JSON response: {str(json_error)}")
                raise HTTPException(status_code=500, detail="Failed to parse JSON response from Lichess API")
        else:
            raise HTTPException(status_code=response.status_code, detail=f"Failed to retrieve rating history for {username} from Lichess API")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
