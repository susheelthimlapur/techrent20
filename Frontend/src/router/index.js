import { createRouter, createWebHistory } from 'vue-router'
import LoginUser from '../components/LoginUser.vue'
import RegisterUser from '../components/RegisterUser.vue'
import ForgotPassword from '../components/ForgotPassword.vue'
import Dashboard from '../components/Dashboard.vue'
import BrowseItems from '../Views/BrowseItems.vue'
import ItemPage from '../components/ItemPage.vue'
import PostItem from '@/Views/PostItem.vue'
import LogOut from '@/components/LogOut.vue'
import Admin from '@/Views/Admin.vue'
import AdminItemList from '@/Views/AdminItemList.vue'
import AdminComplaintList from '@/Views/AdminComplaintList.vue'
import Messages from '@/components/Messages.vue'
import Payment from '@/components/Payment.vue'
import Success from '../components/Success.vue'
import ErrorPage from '../components/ErrorPage.vue'
import Refund from '../components/Refund.vue'
import store from '@/store.js'

const router = createRouter({
  linkExactActiveClass: 'active',
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/login',
      name: 'LoginUser',
      component: LoginUser
    },
    {
      path: '/register',
      name: 'RegisterUser',
      component: RegisterUser
    },
    {
      path: '/forgotpassword',
      name: 'ForgotPassword',
      component: ForgotPassword
    },
    {
      path: '/browse',
      name: 'BrowseItems',
      component: BrowseItems
    },
    {
      path: '/itempage/:id',
      name: 'ItemPage',
      component: ItemPage,
      params: true
    },
    {
      path: '/post',
      name: 'PostItem',
      component: PostItem,
      beforeEnter(to, from, next) {
        let authenticated = window.localStorage.token //store.getters.isAuthenticated
        if (authenticated) {
          next()
        } else {
          next('/login')
        }
      }
    },
    {
      path: '/logout',
      name: 'LogOut',
      component: LogOut
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
      beforeEnter(to, from, next) {
        let authenticated = store.getters.isAuthenticated
        console.log('Authenticated: ' + authenticated)
        console.log('User: ' + JSON.parse(window.localStorage.userData).email)
        if (
          authenticated &&
          JSON.parse(window.localStorage.userData).email == 'admin@test.com'
        ) {
          next()
        } else {
          next('/login')
        }
      },
      children: [
        {
          path: 'items',
          name: 'admin-item-list',
          component: AdminItemList
        },
        {
          path: 'complaints',
          name: 'admin-complaint-list',
          component: AdminComplaintList
        }
      ]
    },
    {
      path: '/messages',
      name: 'Messages',
      component: Messages,
      beforeEnter(to, from, next) {
        let authenticated = store.getters.isAuthenticated
        console.log(authenticated)
        if (authenticated) {
          next()
        } else {
          next('/login')
        }
      }
    },
    {
      path: '/payment',
      name: 'Payment',
      component: Payment
    },
    {
      path: '/success',
      name: 'Success',
      component: Success
    },
    {
      path: '/error',
      name: 'Error',
      component: ErrorPage
    },
    {
      path: '/refund',
      name: 'Refund',
      component: Refund
    }
  ]
})

export default router
