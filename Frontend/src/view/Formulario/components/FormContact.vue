<template>
  <form @submit.prevent>
    <div class="m-5">
      <!-- Fila 1 -->
      <div class="row mb-3">
        <div class="col-md-4">
          <input
            type="text"
            class="form-control"
            placeholder="Name"
            v-model="formData.name"
        
          />
        </div>
        <div class="col-md-4">
          <input
            type="text"
            class="form-control"
            placeholder="Phone"
            v-model="formData.phone"
          />
        </div>
      </div>

      <!-- Fila 2 -->
      <div class="row mb-3">
      
        
      </div>
       <!-- Botones centrados -->
      <div class="row mb-3">
        <div class="col-12 d-flex justify-content-center">
          <FormButtons @save="submitForm" 
          @cancel="redirecto" />
          
        </div>
      </div>

    </div>
  </form>
</template>

<script setup>
import { createContact } from '@/services/contact'  
import FormButtons from '@/components/design/atoms/FormButtons.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const formData = ref({
  name: '',
  phone: ''
})  

const redirecto = () => {
  router.push('forms')
}

const submitForm = () => {
  createContact(formData.value)
    .then(response => {
      console.log('Contact created:', response.data)
      router.push('/forms')
    })
    .catch(error => {
      console.error('Error creating contact:', error)
    })
}

</script>
