<template>
  <div class="position-relative">
    <div class="position-absolute top-2 end-0 p-9">
      <AccionButtons @save="goForm" />
    </div>

   
    <div class="container mt-5 pt-5">
      <DataTable
        :columns="columns"
        :data="contacts"
        @update:selected="selectedRows = $event"
      />
    </div>
  </div>
</template>

<script setup>
import DataTable from '@/components/design/molecules/DataTable.vue'
import AccionButtons from '@/components/design/molecules/AccionButtons.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { getContacts } from '../../services/contact'

const router = useRouter()

const contacts = ref([])
const selectedRows = ref([])

const columns = [
  { key: 'name', label: 'Name' },
  { key: 'phone', label: 'Phone' }
]

const goForm = () => {
  router.push({ name: 'form-forms' })
}
onMounted(async () => {
  try {
    const response = await getContacts()
console.log('Respuesta completa:', response)

//  línea comentada por ahora para no causar el error
// contacts.value = response.data.map(contact => ({
//   name: contact.name,
//   phone: contact.phone
// }))
    console.log('Contactos cargados:', contacts.value)
  } catch (error) {
    console.error('Error al cargar contactos:', error)
  }
})

</script>

<style scoped>
.container {
  margin-top: 80px; 
}
</style>
