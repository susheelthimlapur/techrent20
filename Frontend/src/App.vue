<template>
  <header>
    <LogoLink msg="<TechRent>" />
    <nav>
      <router-link to="/">Home</router-link>
      <router-link v-if="!isAuthenticated" to="/login">Login</router-link>
      <router-link to="/browse">Browse</router-link>
      <router-link v-if="isAuthenticated" to="/post">Post Item</router-link>
      <router-link v-if="isAdmin" to="/admin/items">Admin</router-link>
      <!-- <router-link v-if="isAuthenticated" to="/messages">Messages</router-link> -->
      <!-- <router-link to="/payment">Payment</router-link> -->
      <button v-if="userData.name" class="username" @click="openNav">
        Welcome, {{ userData.name }}
      </button>
      <div id="mySidenav" class="sidenav">
        <ul>
          <li><a @click="closeNav" class="closebtn">&times;</a></li>
          <li>
            <a>Rented Items</a>
          </li>
          <li>
            <a>Account Details</a>
          </li>
          <li>
            <a>
              <router-link v-if="isAuthenticated" to="/messages"
                >Messages</router-link
              >
            </a>
          </li>
          <li>
            <a id="logout" v-if="isAuthenticated" @click="confirmLogout"
              >Log Out</a
            >
          </li>
        </ul>
      </div>
    </nav>
    <div class="all-over-bkg"></div>
  </header>
  <div class="content-wrapper">
    <router-view id="content" />
  </div>
  <footer>
    <div>
      <h2>Contact</h2>
      <ul>
        <li>email: TechRent@gmail.com</li>
        <li>317-123-1234</li>
      </ul>
    </div>
    <div>
      <h2>
        GitHub: <a href="https://github.com/cam-line/TechRent">TechRent</a>
      </h2>
    </div>
  </footer>
</template>

<script>
//import { RouterLink, RouterView } from "vue-router";
import LogoLink from '@/components/LogoLink.vue'
import BrowseItems from '@/Views/BrowseItems.vue'
import { mapState } from 'vuex'
import { authenticate } from './api'

export default {
  data() {
    return { authenticated: false }
  },
  mounted() {
    this.$store.dispatch('loadItems')
    this.$store.dispatch('loadCurrentUser')
  },
  components: {
    LogoLink,
    BrowseItems
  },
  computed: {
    isAuthenticated() {
      // if (!this.$store.getters.isAuthenticated) {
      //   this.authenticated = false
      //   this.$store.dispatch('logout')
      // } else {
      //   this.authenticated = true
      // }
      // return this.$store.getters.isAuthenticated
      this.authenticated = this.$store.getters.isAuthenticated
      console.log('Authenticated = ', this.authenticated)
      return this.authenticated
    },
    isAdmin() {
      console.log(
        'Admin = ',
        window.localStorage.userData &&
          JSON.parse(window.localStorage.userData).email == 'admin@test.com'
      )
      return (
        window.localStorage.userData &&
        JSON.parse(window.localStorage.userData).email == 'admin@test.com'
      )
    },
    confirmLogout(e) {
      let logout = confirm('Are you sure you want to logout?')
      if (logout) {
        this.authenticated = false
        this.$store.dispatch('logout')
      } else {
        e.preventDefault()
      }
    },
    ...mapState(['userData']),
    openNav() {
      document.querySelector('#mySidenav').style.width = '250px'
      document.querySelector('.all-over-bkg').classList.add('is-visible')
    },
    closeNav() {
      document.querySelector('#mySidenav').style.width = '0'
      document.querySelector('.all-over-bkg').classList.remove('is-visible')
    }
  }
}
</script>

<style scoped>
@import './assets/normalize.css';
.content-wrapper {
  min-height: 100%;
}

#content {
  margin: 0 auto;
}

nav {
  font-size: 12px;
  text-align: center;
  justify-content: center;
  margin-top: 2rem;
}

nav a.router-link-active {
  color: var(--color-background);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

#logout {
  color: var(--color-pop);
}

header {
  position: sticky;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: column;
  height: 20vh;
  z-index: 9999999;
  width: 100%;
  background: var(--color-secondary);
  border-bottom: 5px solid var(--color-pop);
  -webkit-box-shadow: 0 3px 5px rgba(57, 63, 72, 0.3);
  -moz-box-shadow: 0 3px 5px rgba(57, 63, 72, 0.3);
  box-shadow: 0 3px 5px rgba(57, 63, 72, 0.3);
  padding: 20px 50px;
}

nav {
  text-align: center;
  margin-left: -1rem;
  font-size: 1rem;
  padding: 1rem 0;
  margin-top: 1rem;
}

/*
  Navigation
*/
.openbtn {
  color: var(--aqua-black);
}

.openbtn:hover {
  cursor: pointer;
  color: var(--aqua-blue);
}

.sidenav ul {
  margin: 0;
  padding: 0;
}

.sidenav li {
  list-style-type: none;
}

.all-over-bkg {
  display: none;
}

.is-visible {
  background-color: rgba(0, 0, 0, 0.4);
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  z-index: 9999;
  display: block;
}

#mySidenav {
  z-index: 10000;
}

.sidenav {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  top: 0;
  right: 0;
  overflow-x: hidden;
  padding-top: 60px;
  transition: 0.5s;
  background-color: var(--color-background);
}

.sidenav ul li a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  display: block;
  transition: 0.3s;
  color: var(--color-secondary);
}

.sidenav .closebtn {
  /* position: absolute;
  top: 0;
  right: 25px; */
  font-size: 36px;
  margin-left: 50px;
}

.subnav li a {
  font-size: 16px;
  margin-left: 1em;
}

@media (min-width: 1024px) {
  header {
    flex-direction: row;
  }
}
</style>
