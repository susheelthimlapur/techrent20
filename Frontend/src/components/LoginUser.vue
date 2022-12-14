<template lang="">
  <div class="login-view">
    <div class="close" @click="routeToDashboard"></div>
    <form @submit.prevent="login">
      <h1 class="">Login</h1>
      <div class="input">
        <label for="email">Email address</label>
        <input
          class="form-input"
          type="text"
          name="email"
          placeholder="email@adress.com"
          v-model="email"
        />
      </div>
      <div class="input">
        <label for="password">Password</label>
        <input
          class="form-input"
          type="password"
          name="password"
          placeholder="password"
          v-model="password"
        />
      </div>
      <div class="login-question">
        <a class="forgot-password" @click="routeToForgotPassword">
          Forgot your password?
        </a>
      </div>
      <div class="login-question">
        Don't have an account?
        <a class="register-account" @click="routeToRegister"> Register </a>
      </div>
      <button type="submit" class="" id="login_button">Login</button>
    </form>
    <div class="or">
      <h4>OR</h4>
      <hr />
    </div>
    <div class="login-with">
      <h3>Login with:</h3>
      <img src="../assets/Google_Logo.png" alt="google logo" id="google" />
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { useStore } from 'vuex'
import axios from 'axios'

export default {
  name: 'LoginUser',
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    // getresponse() {
    //   const path = 'http://localhost:5000/LoginUser'
    //   axios
    //     .get(path)
    //     .then((res) => {
    //       console.log(res.data)
    //       this.msg = res.data
    //     })
    //     .catch((err) => {
    //       console.error(err)
    //     })
    // },
    login() {
      const data = {
        email: this.email,
        password: this.password
      }

      this.$store
        .dispatch('login', data)
        .then(() => this.$router.push('/'))
        .catch((error) => console.log(error))
    },
    routeToForgotPassword() {
      this.$router.push('/forgotpassword')
    },
    routeToDashboard() {
      this.$router.push('/')
    },
    routeToRegister() {
      this.$router.push('/register')
    }
  }
  // created() {
  //   this.getresponse()
  // }
}
</script>
<style scoped>
.login-view {
  position: fixed;
  z-index: 10000;
  top: 55%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 1px solid var(--color-primary);
  padding: 4rem 4rem;
  border-radius: 5px;
  background: var(--color-highlight);
}

.login-question {
  margin-bottom: 10px;
}

button {
  width: 100%;
}

hr {
  height: 0.2rem;
  width: 100%;
  margin-left: 10px;
  border-width: 0;
  background-color: var(--color-tertiary);
}

.or {
  display: flex;
  align-items: center;
  margin: 20px 0;
}

.close:after {
  display: inline-block;
  position: fixed;
  top: 5px;
  right: 20px;
  content: '\00d7';
  font-size: 30px;
}

.close:hover {
  cursor: pointer;
  color: var(--color-pop);
}

#google {
  height: 40px;
  widows: 40px;
}

#google:hover {
  cursor: pointer;
}

.login-with {
  display: flex;
  justify-content: space-between;
}
</style>
