import api from '@/services/api'

export const loginUser = async (credentials) => {
  try {
    const response = await api({
      url: '/auth/login',
      method: 'post',
      data: credentials
    })
    const token = response.data.access_token || response.data.token
    if (token) {
      localStorage.setItem('token', token)
    }

    return response
  } catch (error) {
    console.error(' Error en login:', error)
    throw error
  }
}
