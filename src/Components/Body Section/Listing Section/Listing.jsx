import React from 'react'
import './listing.css'
import { useEffect, useState } from 'react';
import {BsInfoCircle} from 'react-icons/bs'

import chilli from '../../../LoginAssets/pexels-eva-bronzini-5501465.jpg'
import leaf from '../../../LoginAssets/leaf.png'
import sunlogo from '../../../LoginAssets/sunlogo.jpg'
import waterdrop from '../../../LoginAssets/pexels-pixabay-40731.jpg'
import mois from '../../../LoginAssets/moisture.png'
import lum from '../../../LoginAssets/luminosity.png'
import nit from '../../../LoginAssets/nitrogen.png'
import pos from '../../../LoginAssets/phosphorus.png'
import pot from '../../../LoginAssets/potassium.png'

const Listing = () => {
  const [humidity, setHumidity] = useState(null);
  const [temperature, setTemp] = useState(null);
  const [luminosity, setLum] = useState(null);
  const [moisture, setMois] = useState(null);
  const [N, setN] = useState(null);
  const [P, setP] = useState(null);
  const [K, setK] = useState(null);
  

  useEffect(() => {

    const fetchLuminosityData = async () => {
      try {
        const response = await fetch('https://api.thingspeak.com/channels/2146750/fields/1.json?api_key=PNOQX59AGZZYNI98&results=2');
        const data = await response.json();
        setLum(data.feeds[0].field1);
      } catch (error) {
        console.error('Error fetching humidity data:', error);
      }
    };

    const fetchMoisData = async () => {
      try {
        const response = await fetch('https://api.thingspeak.com/channels/2146750/fields/2.json?api_key=PNOQX59AGZZYNI98&results=2');
        const data = await response.json();
        setMois(data.feeds[0].field2);
      } catch (error) {
        console.error('Error fetching moisture data:', error);
      }
    };

    const fetchTempData = async () => {
      try {
        const response = await fetch('https://api.thingspeak.com/channels/2146750/fields/3.json?api_key=PNOQX59AGZZYNI98&results=2');
        const data = await response.json();
        setTemp(data.feeds[0].field3);
      } catch (error) {
        console.error('Error fetching temp data:', error);
      }
    };

    const fetchHumidityData = async () => {
      try {
        const response = await fetch('https://api.thingspeak.com/channels/2146750/fields/4.json?api_key=PNOQX59AGZZYNI98&results=2');
        const data = await response.json();
        setHumidity(data.feeds[0].field4);
      } catch (error) {
        console.error('Error fetching humidity data:', error);
      }
    };

    const fetchNData = async () => {
      try {
        const response = await fetch('https://api.thingspeak.com/channels/2146750/fields/5.json?api_key=PNOQX59AGZZYNI98&results=2');
        const data = await response.json();
        setN(data.feeds[0].field5);
      } catch (error) {
        console.error('Error fetching N data:', error);
      }
    };

    const fetchPData = async () => {
      try {
        const response = await fetch('https://api.thingspeak.com/channels/2146750/fields/6.json?api_key=PNOQX59AGZZYNI98&results=2');
        const data = await response.json();
        setP(data.feeds[0].field6);
      } catch (error) {
        console.error('Error fetching P data:', error);
      }
    };

    const fetchKData = async () => {
      try {
        const response = await fetch('https://api.thingspeak.com/channels/2146750/fields/7.json?api_key=PNOQX59AGZZYNI98&results=2');
        const data = await response.json();
        setK(data.feeds[0].field7);
      } catch (error) {
        console.error('Error fetching K data:', error);
      }
    };

    

    // Fetch data initially
    fetchLuminosityData();
    fetchMoisData();
    fetchTempData();
    fetchHumidityData()
    fetchNData();
    fetchPData();
    fetchKData();

    // Fetch humidity data every 5 seconds
    const intervalIdL = setInterval(fetchLuminosityData, 10000);
    const intervalIdM = setInterval(fetchMoisData, 10000);
    const intervalIdT = setInterval(fetchTempData, 10000);
    const intervalIdH = setInterval(fetchHumidityData, 10000);
    const intervalIdN = setInterval(fetchNData, 10000);
    const intervalIdP = setInterval(fetchPData, 10000);
    const intervalIdK = setInterval(fetchKData, 10000);

    // Clean up the interval on component unmount
    return () => {
      clearInterval(intervalIdL);
      clearInterval(intervalIdM);
      clearInterval(intervalIdT);
      clearInterval(intervalIdH);
      clearInterval(intervalIdN);
      clearInterval(intervalIdP);
      clearInterval(intervalIdK);
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
              <div className="humidity">{humidity} %</div>
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
            {temperature !== null ? (
              <div className="temperature-percentage">{temperature} C</div>
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

            <img src={mois} alt="leaf"/>
            {moisture !== null ? (
              <div className="moisture-percentage">{moisture}</div>
            ) : (
              <div></div>
            )}

            <br />
            <div className="percentageText">
            < BsInfoCircle className ="infoicon"/>
              <span>Daily Moisture</span>
            </div>
          </div>



          <div className="luminosity-container">

            <img src={lum} alt="leaf"/>
            {luminosity !== null ? (
              <div className="luminosity-percentage">{luminosity}</div>
            ) : (
              <div></div>
            )}

            <br />
            <div className="percentageText">
            < BsInfoCircle className ="infoicon"/>
              <span>Luminosity</span>
            </div>
          </div>

           <div className="N-container">

            <img src={nit} alt="leaf"/>
            {N !== null ? (
              <div className="N-percentage">{N} mg/kg</div>
            ) : (
              <div></div>
            )}

            <br />
            <div className="percentageText">
            < BsInfoCircle className ="infoicon"/>
              <span>Nitrogen</span>
            </div>
          </div>


          <div className="P-container">

            <img src={pos} alt="leaf"/>
            {P !== null ? (
              <div className="P-percentage">{P} mg/kg</div>
            ) : (
              <div></div>
            )}

            <br />
            <div className="percentageText">
            < BsInfoCircle className ="infoicon"/>
              <span>Phosphorus</span>
            </div>
          </div>


          <div className="K-container">

            <img src={pot} alt="leaf"/>
            {K !== null ? (
              <div className="K-percentage">{K} mg/kg</div>
            ) : (
              <div></div>
            )}

            <br />
            <div className="percentageText">
            < BsInfoCircle className ="infoicon"/>
              <span>Potassium</span>
            </div>
          </div> 



          
        

        
      </div>
      
    </div>
  )
}

export default Listing