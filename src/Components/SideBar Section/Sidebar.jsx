import React from 'react'
import './Sidebar.css'

import logo from '../../LoginAssets/logo.png'
import plantlogo from '../../LoginAssets/plantlogo3.png'

import {IoMdSpeedometer} from 'react-icons/io'
import {CgProfile} from 'react-icons/cg'

const Sidebar = () => {
  return (
    <div className='sideBar grid'>
      <div className='logoDiv flex'>
        <img src={logo} alt='Image Name'/>
        <h2>Digital Twin</h2>
      </div>

      <div className='menuDiv'>
        <h3 className='divTitle'>
          Quick Menu
        </h3>
        <ul className="menuLists grid">

          <li className="listItem">
            <a href='/' className='menuLink flex'>
              <IoMdSpeedometer className="icon"/>
              <span className="smallText">
                Dash board
              </span>
            </a>
          </li>

          <li className="listItem">
            <a href='/analytics' className='menuLink flex'>
              <CgProfile className="icon"/>
              <span className="smallText">
                Analytics
              </span>
            </a>
          </li>

        </ul>

      </div>

      <div className='plantLogo flex'>
        <img src={plantlogo} alt="plant image" />

      </div>

    </div>
  )
}

export default Sidebar