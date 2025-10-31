import { createRouter, createWebHistory } from 'vue-router'

// Importar rutas por módulo
import homeRoutes from './home.js'
import formRoutes from './form.js'
import loginRoutes from './login.js'

// Combinar todas las rutas en un solo array
const routes = [
  ...loginRoutes,
  ...homeRoutes,
  ...formRoutes
]



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// DEBUG: muestra las rutas registradas
console.log('ROUTER REGISTERED ROUTES:', router.getRoutes().map(r => ({ name: r.name, path: r.path })))
window.__router = router

export default router

