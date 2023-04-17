import { useState } from 'react'
import './App.css'
import { BrowserRouter,Link,Route,Routes } from 'react-router-dom'

import {Home,CreatePost} from './pages';


function App() {

  return (
    <BrowserRouter>
      <headers className='w-full flex justify-between items-center bg-white
                          sm-px8 px4 py-4 border-b border-b-[#e6ef4]'>
        <Link className='w-20 object-contain px-4' to={'/'}><img className='h-10' 
        src="https://seeklogo.com/images/O/open-ai-logo-8B9BFEDC26-seeklogo.com.png" alt="Logo" /></Link>
        <Link className='font-inter font-medium bg-[#6469ff] text-white mx-5 px-4 py-2 rounded-md'
         to={'/create-post'}>Create</Link>
      </headers>
      <main className='sm:p-8 px-4 py-8 w-full bg-[#f9fafe] min-h-[calc(100vh-73px)]'>
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path='/create-post' element={<CreatePost/>}/>
        </Routes>
      </main>
    </BrowserRouter>
  )
}

export default App
