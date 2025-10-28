import { useRouter } from 'vue-router'

export function auth() {
  const router = useRouter()

  const login = async (values) => {
    const { user, password } = values

    if (user === 'admin' && password === '1234') {
      router.push('/dashboard')
    } else {
      alert('Usuario o contraseña incorrectos')
    }
  }

  return { login }
}
