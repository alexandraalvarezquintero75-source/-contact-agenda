import api from "./api";

export const createContact = (contactData) => {
    return new api({
        url: 'contacts',
        method: 'post',
        data: contactData
    })
}