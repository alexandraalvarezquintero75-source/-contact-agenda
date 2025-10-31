<template>
  <div class="d-flex">
    <SidebarMenu />

    <div class="main-layout flex-grow-1 d-flex flex-column min-vh-100">
      <!-- <Header /> -->

      <main class="flex-grow-1 p-3">
        <RouterView />
      </main>

      <!-- <Footer /> -->
    </div>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import SidebarMenu from './components/design/organisms/sidebarMenu.vue'



</script>
