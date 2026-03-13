import axiosClient from './axiosClient'

export const authApi = {
  login: (username, password) => axiosClient.post('/auth/login', { username, password })
}

