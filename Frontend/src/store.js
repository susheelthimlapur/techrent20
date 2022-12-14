import { createStore } from 'vuex'

// imports of AJAX functions will go here
import {
  postNewItem,
  submitNewMessage,
  authenticate,
  register,
  getItems,
  deleteItem,
  getMessages
} from '@/api'

import { isValidJwt } from '@/utils'

const store = createStore({
  state: {
    // single source of data
    items: [],
    currentItem: {},
    messages: [],
    currentMessage: {},
    userData: {},
    jwt: ''
  },

  actions: {
    login(context, userData) {
      console.log(userData)
      return authenticate(userData)
        .then((response) => {
          context.commit('SET_JWT_TOKEN', { jwt: response.data.token })
          context.commit('SET_USER_DATA', response.data.user)
        })
        .catch((error) => {
          console.log('Error Authenticating: ', error)
        })
    },
    register(context, userData) {
      //context.commit('SET_USER_DATA', { userData })
      return register(userData)
        .then(context.dispatch('login', userData))
        .catch((error) => {
          console.log('Error Registering: ', error)
        })
    },
    submitNewItem(context, item) {
      return postNewItem(item, window.localStorage.token)
    },
    submitMessage(context, message) {
      return submitNewMessage(message, window.localStorage.token)
    },
    loadItems(context) {
      return getItems()
        .then((response) => {
          console.log(response.data)
          context.commit('SET_ITEMS', { items: response.data })
        })
        .catch((error) => {
          console.log('Error retrieving items: ', error)
        })
    },
    loadMessages(context) {
      return getMessages()
        .then((response) => {
          console.log(response.data)
          context.commit('SET_MESSAGES', { messages: response.data })
        })
        .catch((error) => {
          console.log('error retrieving messages: ', error)
        })
    },
    deleteItem(context, item) {
      return deleteItem(item, context.state.jwt.token)
    },
    loadCurrentUser(context) {
      let user = window.localStorage.userData
        ? JSON.parse(window.localStorage.userData)
        : {}
      context.commit('SET_USER_DATA', user)
    },
    logout(context) {
      context.commit('SET_USER_DATA', {})
      context.commit('SET_JWT_TOKEN', '')
    }
  },

  mutations: {
    SET_USER_DATA(state, payload) {
      console.log('setUserData payload = ', payload)
      state.userData = payload
      window.localStorage.setItem('userData', JSON.stringify(payload))
    },
    SET_JWT_TOKEN(state, payload) {
      console.log('setJwtToken payload = ', payload)
      localStorage.token = payload.jwt
      state.jwt = payload.jwt
    },
    SET_ITEMS(state, items) {
      state.items = items
    },
    SET_MESSAGES(state, messages) {
      console.log(messages.messages)
      state.messages = messages.messages
      console.log(state.messages)
    }
  },

  getters: {
    isAuthenticated(state) {
      console.log(
        'Valid jwt: ' +
          isValidJwt(window.localStorage.token) +
          ' token = ' +
          window.localStorage.token
      )
      return isValidJwt(window.localStorage.token)
    },
    getUserData(state) {
      console.log(state.userData.email)
      console.log(state.jwt)
      return state.userData
    }
  }
})

export default store
