import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'

const Nav = () => {
  const { logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/')
  }

  return (
    <nav className="bg-blue-600 p-4 text-white">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-xl font-bold">RecSys Shop</Link>
        <div className="space-x-4">
          <Link to="/" className="hover:underline">Home</Link>
          <Link to="/products" className="hover:underline">Products</Link>
          <Link to="/profile" className="hover:underline">Profile</Link>
          <button onClick={handleLogout} className="hover:underline">Logout</button>
        </div>
      </div>
    </nav>
  )
}

export default Nav

