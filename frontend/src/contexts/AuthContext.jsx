import React, { createContext, useContext, useState, useEffect } from 'react'
import axios from 'axios'

const AuthContext = createContext()

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (!context) throw new Error('useAuth must be used within AuthProvider')
  return context
}

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem('token') || '')
  const [userId, setUserId] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
      setUserId(JSON.parse(atob(token.split('.')[1])).sub)
    }
    setLoading(false)
  }, [token])

  const login = async (username, password) => {
    try {
      const response = await authApi.login(username, password)
      const { access_token } = response.data
      localStorage.setItem('token', access_token)
      setToken(access_token)
      return true
    } catch (error) {
      return false
    }
  }

  const logout = () => {
    localStorage.removeItem('token')
    setToken('')
    setUserId(null)
    delete axios.defaults.headers.common['Authorization']
  }

  return (
    <AuthContext.Provider value={{ token, userId, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  )
}

