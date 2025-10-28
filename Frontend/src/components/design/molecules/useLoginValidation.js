import { reactive } from 'vue'
import * as yup from 'yup'

export function useLoginValidation() {
  const values = reactive({
    user: '',
    password: ''
  })

  const errors = reactive({
    user: '',
    password: ''
  })

  const schema = yup.object({
    user: yup.string().required('El usuario es obligatorio'),
    password: yup.string().required('La contraseña es obligatoria')
  })

  async function validate() {
    try {
      await schema.validate(values, { abortEarly: false })
      errors.user = ''
      errors.password = ''
      return true
    } catch (err) {
      errors.user = ''
      errors.password = ''
      err.inner.forEach(e => {
        errors[e.path] = e.message
      })
      return false
    }
  }

  return { values, errors, validate }
}
