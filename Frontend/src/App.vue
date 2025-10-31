<template>
  <div>
    
    <div v-if="!isLoginPage" class="d-flex">
      <SidebarMenu />
      <div class="main-layout flex-grow-1 d-flex flex-column min-vh-100">
        <main class="flex-grow-1 p-3">
          <RouterView />
        </main>
      </div>
    </div>

  
    <div v-else>
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { RouterView, useRoute } from 'vue-router'
import { computed } from 'vue'
import SidebarMenu from './components/design/organisms/sidebarMenu.vue'

const route = useRoute()


const isLoginPage = computed(() => route.path === '/login' || route.path === '/')
</script>
