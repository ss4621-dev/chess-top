// src/components/RatingHistoryChart.js
import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import axios from "axios";

function RatingHistoryChart() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:8000/players/rating-history-csv"
        );
        setPlayers(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  const data = {
    labels: [
      "Day 1",
      "Day 2",
      "Day 3",
      "Day 4",
      "Day 5",
      "Day 6",
      "Day 7",
      "Day 8",
      "Day 9",
      "Day 10",
    ],
    datasets: players.map((player) => ({
      label: player.username,
      data: [player.rating_30_days_ago, ...player.rating_history],
      fill: false,
      borderColor: getRandomColor(),
    })),
  };

  const options = {
    scales: {
      x: {
        title: {
          display: true,
          text: "Days",
        },
      },
      y: {
        title: {
          display: true,
          text: "Rating",
        },
      },
    },
  };

  function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  return (
    <div>
      <h3>Rating History Chart</h3>
      <Line data={data} options={options} />
    </div>
  );
}

export default RatingHistoryChart;
