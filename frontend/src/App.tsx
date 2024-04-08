import { useState, useEffect } from 'react'
import './App.css'
import {server_url} from './appsettings.json'
import AppRouter from './AppRouter'

function App() {
  const [data, setData] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      console.log()
      try{
        const response = await fetch(`${server_url}/event`)
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        const data = await response.json()
        console.log(data)
        setData(data);
      } catch (error) {
        console.log(error)
      
      }
    }
    fetchData()
  }, [])
  return (
    <>
      <AppRouter/>
    </>
  )
}

export default App
