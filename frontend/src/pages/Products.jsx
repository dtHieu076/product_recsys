import { useState, useEffect } from 'react'
import { useAuth } from '../contexts/AuthContext'
import { productsApi } from '../api/productsApi'
import { getOrCreateUserSession } from '../utils/session.js'

const Products = () => {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)
  const { userId } = useAuth()

  useEffect(() => {
    fetchProducts()
  }, [])

  const fetchProducts = async () => {
    try {
      const response = await productsApi.getProducts()
      setProducts(response.data)
    } catch (error) {
      console.error('Error fetching products', error)
    } finally {
      setLoading(false)
    }
  }

  const trackEvent = async (productId, eventType) => {
    if (!userId) return
    const userSession = getOrCreateUserSession()
    try {
      await productsApi.trackEvent(productId, eventType, userSession)
      console.log(`${eventType} tracked for product ${productId}`)
    } catch (error) {
      console.error('Error tracking event', error)
    }
  }

  if (loading) return <div className="text-center">Loading products...</div>

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Products</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {products.map((product) => (
          <div key={product.product_id} className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition">
            <img src={product.image_url || '/placeholder.jpg'} alt={product.product_name} className="w-full h-48 object-cover rounded mb-4" />
            <h3 className="font-bold text-xl mb-2">{product.product_name}</h3>
            <p className="text-2xl font-bold text-blue-600 mb-4">${product.price}</p>
            <p className="text-gray-600 mb-4">{product.brand}</p>
            <div className="space-x-2">
              <button 
                onClick={() => trackEvent(product.product_id, 'view')}
                className="bg-gray-200 px-4 py-2 rounded hover:bg-gray-300"
              >
                View
              </button>
              <button 
                onClick={() => trackEvent(product.product_id, 'cart')}
                className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
              >
                Add to Cart
              </button>
              <button 
                onClick={() => trackEvent(product.product_id, 'purchase')}
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
              >
                Buy Now
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Products

