<!-- Contiene los campos, validaciones y acción de envío -->
<template>
  <form @submit.prevent="onSubmit">
    <div class="mb-3">
      <label for="user" class="form-label">Usuario</label>
      <input
        id="user"
        v-model="values.user"
        type="text"
        class="form-control"
        :class="{ 'is-invalid': errors.user }"
      />
      <div v-if="errors.user" class="invalid-feedback">{{ errors.user }}</div>
    </div>

    <div class="mb-3">
      <label for="password" class="form-label">Contraseña</label>
      <input
        id="password"
        v-model="values.password"
        type="password"
        class="form-control"
        :class="{ 'is-invalid': errors.password }"
      />
      <div v-if="errors.password" class="invalid-feedback">{{ errors.password }}</div>
    </div>

    <button type="submit" class="btn btn-primary w-100">
      Iniciar sesión
    </button>
  </form>
</template>

<script setup>
import { useLoginValidation } from '@/components/design/molecules/useLoginValidation'
import { auth } from '@/services/auth'

const { values, errors, validate } = useLoginValidation()
const { login } = auth()

const onSubmit = async () => {
  if (await validate()) {
    await login(values)
  }
}


</script>
