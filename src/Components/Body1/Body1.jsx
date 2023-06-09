import React, { useRef } from 'react';
import './body1.css'
import Top from './Top Section/Top'
import ImageUpload from './Analysis';

const Body1 = () => {

  return (
    <div className='mainContent'>
      <Top/>
      <div className='bottom flex'>
        <ImageUpload/>
      </div>
    </div>
      
  )
}

export default Body1