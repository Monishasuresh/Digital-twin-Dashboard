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
    element: <div><Sidebar/></div>
  },
  {
    path: '/analytics',
    element: <div><Sidebar/></div>
  },
  {
    path: '/analytics',
    element: <div><Analytics/></div>
  },
  {
    path: '/',
    element: <div><Body/></div>
  }
])


const App = () => {
  return (

    // <div>
    //   <RouterProvider router={router}/>
    // </div>
    

     <div className='container'>
      <RouterProvider router={router}/>
       <Sidebar/>
       <Body/>
     </div>
  )
}

export default App