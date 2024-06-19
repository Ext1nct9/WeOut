import {useState, useEffect} from 'react'
import api from '../api'
import TopBar from '../components/Topbar'
import sunset from '../images/SunsetMtl.jpg'
import { Box, Tab, Tabs } from '@mui/material'

function Home(){
    const [events, setEvents] = useState<any[]>([])
    const [content, setContent] = useState<string>('')
    const [title, setTitle] = useState<string>('')
    const [activeTab, setActiveTab] = useState<string>('all')

    const getEvents = (date: string) => {
        api.get('/api/event/', {
            params: {
                date: date
            }
        })
        .then(response => {
            setEvents(response.data)
        })
        .catch(error => {
            console.log(error)
        })
    }

    const handleChange = (event: React.SyntheticEvent, newValue: string) => {
        setActiveTab(newValue)
        getEvents(newValue)
    }

    useEffect(() => {
        getEvents(activeTab)
    }, [])


    return (
        <div>
            <img src={sunset} alt="Description of the image" style={{width: '100vw', height: '50vh', objectFit: 'cover', position: 'absolute', zIndex: -1}} />
            <TopBar/>
            <h1 style = {{paddingTop: '45vh'}}>Trending Events in Montreal</h1>
            <Box sx={{ width: '100%', typography: 'body1' }}>
                <Tabs value={activeTab} onChange={handleChange}>
                    <Tab label="All" value="all" />
                    <Tab label="Today" value="today" />
                    <Tab label="Tomorrow" value="tomorrow" />
                    <Tab label="This Week" value="week" />
                    <Tab label="This Month" value="month" />
                </Tabs>
            </Box>
        </div>
    )
}

export default Home