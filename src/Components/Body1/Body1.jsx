import React, { useRef } from 'react';
import './body1.css'
import Top from './Top Section/Top'
// import ImageUploader from '../Image/ImageUploader';
import LiveStream from '../Image/LiveStream'
import MyComponent from '../Image/MyComponent';

const Body1 = () => {

  return (
    <div className='mainContent'>
      <Top/>
      <div className='bottom flex'>
        <MyComponent/>
        {/* <ImageUploader/> */}
        <LiveStream/>
      </div>
    </div>
      
  )
}

export default Body1