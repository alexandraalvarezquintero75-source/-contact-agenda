<template>
  <div class="d-flex align-items-center justify-content-center vh-100 bg-light">
    <div class="card p-4 shadow" style="width: 400px;">
      <h3 class="text-center mb-3">Iniciar sesión</h3>

      <div class="mb-3">
        <label class="form-label">Correo electrónico</label>
        <input v-model="email" type="email" class="form-control" />
      </div>

      <div class="mb-3">
        <label class="form-label">Contraseña</label>
        <input v-model="password" type="password" class="form-control" />
      </div>

      <button class="btn btn-success w-100" @click="login">Entrar</button>

      <p v-if="errorMessage" class="text-danger mt-3 text-center">
        {{ errorMessage }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { loginUser } from '@/services/auth' // 👈 importa tu endpoint

const email = ref('')
const password = ref('')
const errorMessage = ref('')
const router = useRouter()

const login = async () => {
  try {
    const response = await loginUser({
      email: email.value,
      password: password.value
    })

    const token = response.data.access_token
    localStorage.setItem('token', token) // Guarda el token para futuras peticiones

    router.push('/home') 

  } catch (error) {
    if (error.response?.status === 404) {
      errorMessage.value = 'Correo electrónico no registrado'
    } else if (error.response?.status === 401) {
      errorMessage.value = 'Contraseña incorrecta'
    } else {
      errorMessage.value = 'Error al iniciar sesión'
    }
  }
}
</script>
