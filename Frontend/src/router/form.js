import IndexForm from '@/view/Formulario/IndexForm.vue'
import Form from '@/view/Formulario/components/FormContact.vue'

export default [
  {
    path: '/forms',
    name: 'forms',
    component: IndexForm
  },
  {
    path: '/form-forms',
    name: 'form-forms',
    component: Form
  }
]
