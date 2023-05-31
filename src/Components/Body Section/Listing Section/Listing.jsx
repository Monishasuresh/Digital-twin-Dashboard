import React from 'react'
import './listing.css'
import { useEffect, useState } from 'react';
import {BsInfoCircle} from 'react-icons/bs'

import chilli from '../../../LoginAssets/pexels-eva-bronzini-5501465.jpg'
import leaf from '../../../LoginAssets/leaf.png'
import sunlogo from '../../../LoginAssets/sunlogo.jpg'
import waterdrop from '../../../LoginAssets/pexels-pixabay-40731.jpg'

const Listing = () => {
  const [humidity, setHumidity] = useState(null);

  useEffect(() => {
    const fetchHumidityData = async () => {
      try {
        const response = await fetch('https://api.thingspeak.com/channels/2146750/fields/5.json?api_key=PNOQX59AGZZYNI98&results=2');
        const data = await response.json();
        setHumidity(data.feeds[0].field5);
      } catch (error) {
        console.error('Error fetching humidity data:', error);
      }
    };

    // Fetch humidity data initially
    fetchHumidityData();

    // Fetch humidity data every 5 seconds
    const intervalId = setInterval(fetchHumidityData, 5000);

    // Clean up the interval on component unmount
    return () => {
      clearInterval(intervalId);
    };
  }, []);

 



  return (
    <div className='listingSection'>
      <div className="paramContainer">
        <div className="header">
          <img src={chilli} alt="chilli" />
          <h1 className='imageTitle' >Chilli</h1>
        </div>

        
          <div className="humidity-container">

            <img src={leaf} alt="leaf"/>
            {humidity !== null ? (
              <div className="humidity-percentage">{humidity}%</div>
            ) : (
              <div></div>
            )}

            <br />
            <div className="percentageText">
            < BsInfoCircle className ="infoicon"/>
              <span>Humidity Percentage</span>
            </div>
          </div>


          <div className="temperature-container">

            <img src={sunlogo} alt="leaf"/>
            {humidity !== null ? (
              <div className="temperature-percentage">{humidity}%</div>
            ) : (
              <div></div>
            )}

            <br />
            <div className="percentageText">
            < BsInfoCircle className ="infoicon"/>
              <span>Today's Temperature </span>
            </div>
          </div>



          <div className="moisture-container">

            <img src={waterdrop} alt="leaf"/>
            {humidity !== null ? (
              <div className="moisture-percentage">{humidity}%</div>
            ) : (
              <div></div>
            )}

            <br />
            <div className="percentageText">
            < BsInfoCircle className ="infoicon"/>
              <span>Daily Moisture</span>
            </div>
          </div>

          
        

        
      </div>
      
    </div>
  )
}

export default Listing