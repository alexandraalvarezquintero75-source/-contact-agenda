<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500">
    <div class="bg-white shadow-lg rounded-xl p-8 w-full max-w-md">
      <h2 class="text-2xl font-bold text-center text-gray-800 mb-6">Iniciar Sesión</h2>

      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block text-gray-700 font-medium mb-1" for="email">Correo</label>
          <input
            type="email"
            id="email"
            v-model="email"
            required
            placeholder="tucorreo@ejemplo.com"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <div>
          <label class="block text-gray-700 font-medium mb-1" for="password">Contraseña</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
            placeholder="********"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-indigo-600 text-white py-2 rounded-lg font-semibold hover:bg-indigo-700 transition-colors"
        >
          Entrar
        </button>
      </form>

      <p class="mt-4 text-center text-gray-500 text-sm">
        ¿No tienes cuenta?
        <router-link to="/register" class="text-indigo-600 hover:underline">Regístrate</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'


const email = ref('')
const password = ref('')

</script>

<style scoped>
body {
  font-family: 'Inter', sans-serif;
}
</style>
