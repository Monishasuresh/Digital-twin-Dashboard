import React from 'react'
import './app.css'
import Sidebar from './Components/SideBar Section/Sidebar'
import Body from './Components/Body Section/Body'
import Analytics from './Components/Analytics/Analytics'

import{
  createBrowserRouter,
  RouterProvider
}from 'react-router-dom'

const router = createBrowserRouter([
  {
    path: '/',
    element: <div></div>
  },
  {
    path: '/analytics',
    element: <div> <Analytics/></div>
  }
  
])


const App = () => {
  return (
    <div className='container'>
    <RouterProvider router={router}/>
       <Sidebar/> 
       <Body/>
    </div>
  )
}


export default App