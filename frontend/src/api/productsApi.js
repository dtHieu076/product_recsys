import axiosClient from './axiosClient'

export const productsApi = {
  getProducts: (params = {}) => axiosClient.get('/products', { params }),
  trackEvent: (productId, eventType, userSession) => axiosClient.post(`/products/${productId}/${eventType}`, { user_session: userSession }),
  getRecommendations: () => axiosClient.get('/products/recs')
}

