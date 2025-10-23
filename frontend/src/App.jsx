import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    // FastAPIのエンドポイントへリクエスト
    fetch('http://localhost:8000/')
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
        setMessage('Error connecting to backend');
      });
  }, []);

  return (
    <div className="App">
      <h1>Lie4ML - Frontend</h1>
      <p>Backendからのメッセージ：{message}</p>
    </div>
  );
}

export default App;
