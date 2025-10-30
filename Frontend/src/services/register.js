import api from '@/services/api'

export const registerUser = (userData) => {
  return new api({
    url: 'auth/register',
    method: 'post',
    data: userData
  })
}
