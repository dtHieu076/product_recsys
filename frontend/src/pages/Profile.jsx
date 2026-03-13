import { useState, useEffect } from 'react'
import { useAuth } from '../contexts/AuthContext'
import { productsApi } from '../api/productsApi'

const Profile = () => {
  const [recs, setRecs] = useState([])
  const [loading, setLoading] = useState(true)
  const { logout } = useAuth()

  useEffect(() => {
    fetchRecs()
  }, [])

  const fetchRecs = async () => {
    try {
      const response = await productsApi.getRecommendations()
      setRecs(response.data.recommendations)
    } catch (error) {
      console.error('Error fetching recs', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) return <div className="text-center">Loading recommendations...</div>

  return (
    <div>
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Your Recommendations</h1>
        <button onClick={logout} className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">
          Logout
        </button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {recs.map((product) => (
          <div key={product.product_id} className="bg-white p-6 rounded-lg shadow-md">
            <img src={product.image_url || '/placeholder.jpg'} alt={product.product_name} className="w-full h-48 object-cover rounded mb-4" />
            <h3 className="font-bold text-xl mb-2">{product.product_name}</h3>
            <p className="text-2xl font-bold text-blue-600">${product.price}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Profile

