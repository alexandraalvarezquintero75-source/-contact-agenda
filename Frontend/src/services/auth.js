

import { useRouter } from 'vue-router'
import api from '@/services/api'
import Swal from 'sweetalert2'

export function auth() {
  const router = useRouter()

  const login = async (values) => {
    try {

      const formData = new URLSearchParams()
      formData.append('username', values.user)  
      formData.append('password', values.password)

      const response = await api.post('/login', formData, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      })

      console.log('Login exitoso:', response.data)
      localStorage.setItem('access_token', response.data.access_token)

      await Swal.fire({
        icon: 'success',
        title: '¡Éxito!',
        text: response.data.message,
        confirmButtonText: 'Aceptar'
      })

      router.push('/dashboard')

    } catch (error) {
      if (error.response) {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: error.response.data.detail,
          confirmButtonText: 'Aceptar'
        })
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'No se pudo conectar con el servidor',
          confirmButtonText: 'Aceptar'
        })
      }
    }
  }

  return { login }
}
