import {useState, useEffect} from 'react'
import api from '../api'

function Home(){
    const [events, setEvents] = useState<any[]>([])
    const [content, setContent] = useState<string>('')
    const [title, setTitle] = useState<string>('')

    const getEvents = () => {
        api.get('/api/event/')
        .then(response => {
            setEvents(response.data)
        })
        .catch(error => {
            console.log(error)
        })
    }
    return (
        <div>
            <h1>Home</h1>
        </div>
    )
}

export default Home