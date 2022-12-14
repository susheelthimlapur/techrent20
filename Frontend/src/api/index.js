import axios from 'axios'

const path = 'http://127.0.0.1:5000'

export function postNewItem(item, jwt) {
  return axios.post(`${path}/items/`, item, {
    headers: { Authorization: `Bearer: ${jwt}` }
  })
}
export function submitNewMessage(message, jwt) {
  return axios.post(`${path}/messages`, message, {
    headers: { Authorization: `Bearer: ${jwt}` }
  })
}

export function getItems() {
  return axios.get(`${path}/items`)
}

export function getMessages() {
  return axios.get(`${path}/messages`)
}

export function deleteItem(item, jwt) {
  return axios.delete(`${path}/items/${item.id}`, {
    headers: { Authorization: `Bearer: ${jwt}` }
  })
}

export function authenticate(userData) {
  return axios.post(`${path}/login`, userData)
}

export function register(userData) {
  return axios.post(`${path}/register`, userData)
}
