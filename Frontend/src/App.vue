<template>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
import api from './services/api.js'
import { onMounted } from 'vue';

onMounted(async () => {
  try {
    const res = await api.get("/login")
    console.log(" Conexión exitosa con backend:", res.data)
  } catch (error) {
    console.error(" Error al conectar con backend:", error)
  }
})

</script>
