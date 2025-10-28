import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/view/auth/LoginView.vue'
import DashboardView from '@/view/dashboard/DashboardView.vue'
import RegisterView from '@/view/auth/RegisterView.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
