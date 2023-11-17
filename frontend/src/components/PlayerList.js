// src/components/PlayerList.js
import React, { useEffect, useState } from "react";
import axios from "axios";

function PlayerList() {
  const [topPlayers, setTopPlayers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/top-players");
        setTopPlayers(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h3>Top Players</h3>
      <ul>
        {topPlayers.map((player) => (
          <li key={player.username}>
            {player.username} - {player.rating}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PlayerList;
