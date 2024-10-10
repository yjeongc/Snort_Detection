import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import './Dashboard.css';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const Dashboard = () => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    // Django API에서 탐지 결과를 가져옴
    axios.get('http://127.0.0.1:8000/api/alerts/')
      .then(response => {
        setAlerts(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  // 데이터 시각화를 위한 구성
  const data = {
    labels: alerts.map((alert, index) => `Alert ${index + 1}`),
    datasets: [
      {
        label: 'Snort Alerts',
        data: alerts.map(alert => alert.id),
        backgroundColor: 'rgba(75,192,192,0.6)',
      },
    ],
  };

  return (
    <div className="dashboard-container">
      {/* 표를 차트보다 위로 이동 */}
      <h3>Snort Alerts Table</h3>
      <table className="alerts-table">
        <thead>
          <tr>
            <th style={{ backgroundColor: '#FF7F7F' }}>ID</th>
            <th style={{ backgroundColor: '#FF7F7F' }}>Timestamp</th>
            <th style={{ backgroundColor: '#4CAF50' }}>Alert Message</th>
            <th style={{ backgroundColor: '#4CAF50' }}>Source IP</th>
            <th style={{ backgroundColor: '#FFBF00' }}>Destination IP</th>
            <th style={{ backgroundColor: '#FFBF00' }}>Protocol</th>
          </tr>
        </thead>
        <tbody>
          {alerts.map((alert, index) => (
            <tr key={alert.id} style={{ backgroundColor: index % 2 === 0 ? '#FFF2CC' : '#FFE699' }}>
              <td>{alert.id}</td>
              <td>{alert.timestamp}</td>
              <td>{alert.alert_message}</td>
              <td>{alert.source_ip}</td>
              <td>{alert.destination_ip}</td>
              <td>{alert.protocol}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Snort Alerts Dashboard</h2>
      {alerts.length > 0 ? <Bar data={data} /> : <p>Loading data or no alerts available...</p>}
    </div>
  );
};

export default Dashboard;