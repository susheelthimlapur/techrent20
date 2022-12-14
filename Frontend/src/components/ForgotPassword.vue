<template lang="">
  <div class="container">
    <div class="forgotPassword-view">
      <div class="close" @click="routeToDashboard"></div>

      <form @submit.prevent="forgotpassword">
        <h2 class="">Forgot Password</h2>

        <div class="input">
          <label for="email">Email address</label>
          <input
            class="form-input"
            type="text"
            name="email"
            placeholder="email@address.com"
          />
        </div>
        <div class="input">
          <label for="question1">What is your mother's maiden name?</label>
          <input class="form-input" type="text" name="question1" />
        </div>
        <div class="input">
          <label for="question2">What high school did you go to?</label>
          <input class="form-input" type="text" name="question2" />
        </div>
        <button type="submit" class="" id="continue_button">Continue</button>
      </form>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { ref } from "vue";
import { useStore } from "vuex";

export default {
  name: "ForgotPassword",
  setup() {
    const store = useStore();
    const router = useRouter();
    const email = ref("");
    const question1 = ref("");
    const question2 = ref("");
    const error = ref(null);

    const credentials = async () => {
      try {
        await store.dispatch("forgotpassword", {
          email: email.value,
          question1: question1.value,
          question2: question2.value,
        });

        router.push("/");
      } catch (err) {
        error.value = err.message;
      }
    };
    return { credentials, email, question1, question2, error };
  },

  methods: {
    routeToRegister() {
      this.$router.push("/register");
    },
    routeToForgotPassword() {
      this.$router.push("/forgotpassword");
    },
    routeToDashboard() {
      this.$router.push("/");
    },
  },
};
</script>

<style>
.forgotPassword-view {
  position: fixed;
  z-index: 10000;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 1px solid var(--color-primary);
  padding: 4rem 4rem;
  border-radius: 5px;
  background: var(--color-highlight);
}

.close:after {
  display: inline-block;
  position: fixed;
  top: 5px;
  right: 20px;
  content: "\00d7";
  font-size: 30px;
}

.close:hover {
  cursor: pointer;
  color: var(--color-pop);
}
</style>
