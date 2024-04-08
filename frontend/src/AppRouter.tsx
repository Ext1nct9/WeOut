import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'
import Event from "./Event"


const AppRouter = () => {
    return (
        <Router>
            <Routes>
                <Route path="/event" element={<Event/>} />
                {/*
                <Route path="/login" component={Login} />
                <Route path="/register" component={Register} />
                <Route path="/event/:id" component={EventDetail} />
                <Route path="/profile" component={Profile} />
                <Route path="/create-event" component={CreateEvent} />
                <Route path="/edit-event/:id" component={EditEvent} />
                <Route path="/edit-profile" component={EditProfile} />
                <Route path="/logout" component={Logout} />
                <Route path="/" component={Home} />
                */}
            </Routes>
        </Router>
        )
    }

    export default AppRouter