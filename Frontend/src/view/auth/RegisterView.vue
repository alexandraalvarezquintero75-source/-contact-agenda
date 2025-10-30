<template>
  <div class="container mt-5" style="max-width: 400px;">
    <h2 class="text-center mb-3">Registro</h2>

    <form @submit.prevent="onSubmit">
      <!-- Email -->
      <div class="mb-3">
        <label for="email" class="form-label">Correo electrónico</label>
        <input
          id="email"
          v-model="values.email"
          type="email"
          class="form-control"
          :class="{ 'is-invalid': errors.email }"
          placeholder="ejemplo@correo.com"
        />
        <div v-if="errors.email" class="invalid-feedback">{{ errors.email }}</div>
      </div>

      <!-- Contraseña -->
      <div class="mb-3">
        <label for="password" class="form-label">Contraseña</label>
        <input
          id="password"
          v-model="values.password"
          type="password"
          class="form-control"
          :class="{ 'is-invalid': errors.password }"
          placeholder="********"
        />
        <div v-if="errors.password" class="invalid-feedback">{{ errors.password }}</div>
      </div>

      <button type="submit" class="btn btn-success w-100">
        Registrar
      </button>

      <div class="text-center mt-3">
        <span
          class="text-primary"
          style="cursor: pointer; text-decoration: underline;"
          @click="goToLogin"
        >
          Volver al inicio de sesión
        </span>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { registerUser } from '@/services/register'
import Swal from 'sweetalert2'


const router = useRouter()
const values = ref({
  email: '',
  password: ''
})
const errors = ref({})


const onSubmit = async () => {
  try {
    await registerUser(values.value)

    await Swal.fire({
      icon: 'success',
      title: 'Registro exitoso',
      text: 'Tu cuenta ha sido creada correctamente.',
      confirmButtonColor: '#28a745'
    })

    router.push('/')
  } catch (error) {

    if (error.response && error.response.data && error.response.data.errors) {
      errors.value = error.response.data.errors
    } else {

      await Swal.fire({
        icon: 'error',
        title: 'Error en el registro',
        text: 'Ha ocurrido un error inesperado. Por favor, intenta nuevamente más tarde.',
        confirmButtonColor: '#dc3545'
      })
    }
  }
}


const goToLogin = () => {
  router.push('/')
}
</script>
