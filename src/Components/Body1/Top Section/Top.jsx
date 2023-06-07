import React from 'react'
import './top.css'

import { useState, useEffect } from 'react';

const Top = () => {

  const [currentDate, setCurrentDate] = useState('');

  useEffect(() => {
    const interval = setInterval(() => {
      const date = new Date();
      const options = { weekday: 'long', day: 'numeric', month: 'short', year: 'numeric' };
      const formattedDate = date.toLocaleDateString('en-IN', options);
      setCurrentDate(formattedDate);
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  


  return (
    <div className='topSection'>
      <div className='headerSection flex'>
        <div className='title'>
        <h1>Welcome Back!</h1>
        
        <p>{currentDate}</p>

        </div>

        

      </div>
    </div>
  )
}

export default Top