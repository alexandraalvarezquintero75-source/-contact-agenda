import api from "./api";

// Crear un nuevo contacto para el usuario autenticado
export const createContact = (contactData) => {
    return new api({
        url: 'contacts',
        method: 'post',
        data: contactData
    })
}
// Obtener todos los contactos del usuario autenticado
export const getContacts = () => {
    return api({
        url: 'Contacts',
        method: 'get'
    })
}