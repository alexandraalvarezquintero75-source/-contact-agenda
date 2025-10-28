import axios from 'axios'
import Swal from 'sweetalert2'

export function useLogin() {
  const login = async (values) => {
    try {

      const { data } = await axios.post('/api/login', values)

      Swal.fire({
        icon: 'success',
        title: 'Bienvenido',
        text: `Hola ${data.user?.name || values.user}`
      })
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Error al iniciar sesión',
        text: error.response?.data?.message || 'Credenciales incorrectas'
      })
    }
  }

  return { login }
}
