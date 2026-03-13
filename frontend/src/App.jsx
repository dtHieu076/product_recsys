import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'

import Login from './pages/Login.jsx'
import Products from './pages/Products.jsx'
import Profile from './pages/Profile.jsx'
import Nav from './components/Nav.jsx'

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <Nav />
        <main className="container mx-auto p-8">
          <Routes>
            <Route path="/" element={<h1 className="text-3xl font-bold">Welcome to Product RecSys Demo</h1>} />
            <Route path="/login" element={<Login />} />
            <Route path="/products" element={<Products />} />
            <Route path="/profile" element={<Profile />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App

