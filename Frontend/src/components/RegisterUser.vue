<template lang="">
  <div class="container">
    <div class="register-view">
      <div class="close" @click="routeToDashboard"></div>
      <form @submit.prevent="register">
        <h1 class="">Register</h1>
        <div class="input">
          <label for="name">Name</label>
          <input
            class="form-input"
            type="text"
            name="name"
            v-model="name"
            placeholder="Johnny Appleseed"
          />
        </div>
        <div class="input">
          <label for="email">Email address</label>
          <input
            class="form-input"
            type="text"
            name="email"
            v-model="email"
            placeholder="email@adress.com"
          />
        </div>
        <div class="input">
          <label for="password">Password</label>
          <input
            class="form-input"
            type="password"
            name="password"
            v-model="password"
            placeholder="password"
          />
        </div>
        <div class="or">
          <h4>Security Questions</h4>
          <hr />
        </div>
        <div class="input">
          <label for="question1">What is your mother's maiden name?</label>
          <input
            class="form-input"
            type="text"
            v-model="question1"
            name="question1"
          />
        </div>
        <div class="input">
          <label for="question2">What high school did you go to?</label>
          <input
            class="form-input"
            type="text"
            name="question2"
            v-model="question2"
          />
        </div>
        <div class="test">
          <h1>
            {{ msg }}
          </h1>
        </div>
        <button type="submit" class="" id="register_button">Register</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterUser',
  data() {
    return {
      name: '',
      email: '',
      password: '',
      question1: '',
      question2: ''
    }
  },
  methods: {
    register() {
      const data = {
        name: this.name,
        email: this.email,
        password: this.password,
        question1: this.question1,
        question2: this.question2
      }

      this.$store.dispatch('register', data).then(() => this.$router.push('/'))
    }
    // axios
    //   .post('http://127.0.0.1:5000/register', data)
    //   .then((res) => {
    //     console.log(res)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
  }
}
</script>

<style>
.register-view {
  position: fixed;
  z-index: 10000000000;
  top: 70%;
  left: 50%;
  transform: translate(-50%, -65%);
  border: 1px solid var(--color-primary);
  padding: 4em 4rem;
  border-radius: 5px;
  background: var(--color-highlight);
}

#register_button {
  width: 100%;
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
</style>
