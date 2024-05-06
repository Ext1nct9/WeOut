import React, { useState, useEffect } from 'react';
import { server_url } from '../appsettings.json';
import {List, ListItem, ListItemText} from '@mui/material'

type Event = {
    created_at: string;
    date: string;
    description: string;
    id: string;
    location: string;
    manager: string;
    time: string;
    title: string;
    updated_at: string;
    visibility: boolean;
};

const Event: React.FC = () => {

    console.log('Rendering Event component...'); // Add console log here
    const [events, setEvents] = useState<Event[]>([]);
    const [filteredEvents, setFilteredEvents] = useState<Event[]>([]);
    const [searchValue, setSearchValue] = useState('');

    const fetchEvents = async () => {
        try {
            const response = await fetch(`${server_url}/api/event`);
            const data = await response.json();
            setEvents(data);
            setFilteredEvents(data);
        } catch (error) {
            console.error('Error fetching events:', error);
        }
    };

    useEffect(() => {
        fetchEvents();
    }, []);

    const handleSearch = (title: string) => {
        if (title) {
            const filtered = events.filter((event) => event.title.includes(title));
            setFilteredEvents(filtered);
        } else {
            setFilteredEvents(events); // reset filteredEvents to be the same as events
        }
    };


    return (
        <div>
            <h1>Events</h1>
            <div>
                <input type="text" placeholder="Search by title" onChange={(e) => setSearchValue(e.target.value)} />
                <button onClick={() => handleSearch(searchValue)}>Filter</button>
            </div>
            <List>
                {filteredEvents.map((event) => (
                    <ListItem key={event.id}>
                        <ListItemText primary={`Title: ${event.title}`} secondary={`Description: ${event.description}`} />
                    </ListItem>
                ))}
            </List>
        </div>
    );
};

export default Event;