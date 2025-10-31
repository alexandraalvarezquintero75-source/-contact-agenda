import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null
  }),
  actions: {
    login(username, password) {
      // Aquí puedes reemplazar por tu API real si quieres
      if (username === 'admin' && password === '1234') {
        this.user = { username }
        localStorage.setItem('user', JSON.stringify(this.user))
        return true
      }
      return false
    },
    logout() {
      this.user = null
      localStorage.removeItem('user')
    },
    loadUser() {
      const savedUser = localStorage.getItem('user')
      if (savedUser) this.user = JSON.parse(savedUser)
    },
    isAuthenticated() {
      return this.user !== null
    }
  }
})
