import { useRouter } from 'vue-router'

export function useLogin() {
  const router = useRouter()

  const login = async (values) => {
    const { user, password } = values

    if (user === 'admin' && password === '1234') {
      // Si el login es exitoso, redirige al dashboard
      router.push('/dashboard')
    } else {
      alert('Usuario o contraseña incorrectos')
    }
  }

  return { login }
}
