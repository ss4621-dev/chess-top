// src/App.js
import React from "react";
import RatingHistoryChart from "./components/RatingHistoryChart";
import PlayerList from "./components/PlayerList";

function App() {
  return (
    <div>
      <h1>Chess App</h1>
      <RatingHistoryChart />
      <PlayerList />
    </div>
  );
}

export default App;
