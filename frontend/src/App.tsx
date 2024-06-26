
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import ProtectedRoute from './components/ProtectedRoute'
import Event from './pages/Event'
import Search from './pages/Search'

function Logout(){
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout(){
  localStorage.clear()
  return <Register/>
}


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element ={<Home/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/register" element={<RegisterAndLogout/>}/>
        <Route path="/logout" element={<Logout/>}/>
        <Route path="*" element={<NotFound/>}/>
        <Route path="/event" element={<Event/>}/>
        <Route path= "/search" element={<Search/>}/>
      </Routes>
    </BrowserRouter>
  )

}

export default App
