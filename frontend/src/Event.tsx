import React, { useState, useEffect } from 'react';
import { server_url } from './appsettings.json';

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
    const [events, setEvents] = useState<Event[]>([]);

    useEffect(() => {
        fetchEvents();
    }, []);

    const fetchEvents = async () => {
        try {
            const response = await fetch(`${server_url}/event`);
            const data = await response.json();
            setEvents(data);
        } catch (error) {
            console.error('Error fetching events:', error);
        }
    };

    return (
        <div>
            {events.map((event) => (
                <div key={event.id}>
                    <h2>{event.title}</h2>
                    <p>{event.description}</p>
                    <p>{event.location}</p>
                    <p>{event.manager}</p>
                    <p>{event.date}</p>
                    <p>{event.time}</p>
                </div>
            ))}
        </div>
    );
};

export default Event;