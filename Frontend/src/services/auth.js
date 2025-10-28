import { useRouter } from 'vue-router'
import api from '@/services/api'
import Swal from 'sweetalert2'

export function auth() {
  const router = useRouter()

  const login = async (values) => {
    try {
      console.log('Valores enviados al login:', values.user, values.password)


      const response = await api.post('/auth/login', {
        email: values.user,      // asegúrate que sea el mismo nombre que el backend espera
        password: values.password
      }, {
        headers: { 'Content-Type': 'application/json' }
      })

      console.log('Login exitoso:', response.data)


      localStorage.setItem('access_token', response.data.access_token)

      await Swal.fire({
        icon: 'success',
        title: '¡Éxito!',
        text: response.data.message || 'Inicio de sesión correcto',
        confirmButtonText: 'Aceptar'
      })

      router.push('/dashboard')

    } catch (error) {
      console.error('Error al iniciar sesión:', error)

      if (error.response) {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: error.response.data.detail || 'Credenciales incorrectas o error en el servidor',
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
