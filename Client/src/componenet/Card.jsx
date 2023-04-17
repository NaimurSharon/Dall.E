import React from 'react'
import {BiDownload} from 'react-icons/bi'
import { downloadImage } from '../utils'

function Card({id,name,photo,prompt}) {
  return (
    <div className='rounded-xl group relative shadow-card mt-4 hover:shadow-cardhover card'>
      <img src={photo} className='w-full h-auto object-cover rounded-xl' alt={prompt} />
      <div className='absolute group-hover:flex flex-col max-h-[94.5%]
      hidden bottom-0 left-0 right-0 bg-[#10131f] m-0 p-3 rounded-md'>
        <p className='text-white text-md overflow-y-auto'>{prompt ? prompt : 'None'}</p>
        <div className='mt-5 flex justify-between items-center gap-2'>
          <div className='flex items-center gap-2'>
            <div className='w-7 h-7 rounded-full object-cover bg-green-700
            flex justify-center items-center text-white text-xs font-bold'>
              {name[0]}
            </div>
            <p className='text-white text-sm'>{name}</p>
          </div>
          <div className='w-12'>
          <button type='button' onClick={()=>downloadImage(id,photo)} className='outline-none bg-transparent border-none'>
            <BiDownload className='text-white w-6 h-6' />
          </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Card