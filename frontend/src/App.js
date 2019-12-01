import React, { useEffect } from 'react';
import './App.css';
import CustomForm from './components/Form/Form';
import axios from 'axios';

function App() {
  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/delete_expired/')
      .then(res => console.log('deleted'))
      .catch(err => console.log(err.message));
  }, []);

  return (
    <div className='App'>
      <h1>Gentle URL Shortener </h1>
      <CustomForm />
    </div>
  );
}

export default App;
