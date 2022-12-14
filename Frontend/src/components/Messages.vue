<template lang="">
  <div class="container">
    <div class="banner image-banner">
      <div class="banner-container">
        <div class="banner-section1">
          <h1>Messages</h1>
        </div>
      </div>
    </div>
    <div class="d-flex flex-column align-items-stretch flex-shrink-0 bg-white">
      <!-- <a
        href="/"
        class="d-flex align-items-center flex-shrink-0 p-3 link-dark text-decoration-none border-bottom"
      > -->
      <svg class="bi pe-none me-2" width="30" height="24">
        <use xlink:href="#bootstrap"></use>
      </svg>
      <span class="fs-5 fw-semibold">Username</span>
      <!-- </a> -->
      <div
        v-for="message in filteredMessages"
        class="list-group list-group-flush border-bottom scrollarea"
      >
        <a
          href="#"
          class="list-group-item list-group-item-action active py-3 lh-sm"
          aria-current="true"
        >
          <div class="d-flex w-100 align-items-center justify-content-between">
            <strong class="mb-1"
              >Message from {{ message.sender_username }}</strong
            >
            <small>{{ message.sent_at }}</small>
          </div>
          <div class="col-10 mb-1 small">
            {{ message.message }}
          </div>
        </a>
      </div>
      <br />
      <br />
      <br />
      <hr />
      <h1>Send a Message</h1>
      <form @submit.prevent="sendMessage">
        <div class="input">
          <input
            placeholder="Write Message"
            type="text"
            name="message"
            v-model="message"
          />
        </div>
        <br />
        <div class="input">
          <input
            placeholder="Recipient"
            type="text"
            name="recipient"
            v-model="recipient"
          />
        </div>
        <br />
        <button type="submit" class="" id="login_button">Send</button>
      </form>
      <br />
      <br />
    </div>
  </div>
</template>
<script>
import { email, required } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'
import { mapState } from 'vuex'
export default {
  name: 'SendMessage',
  setup() {
    return { v$: useVuelidate() }
  },
  data() {
    return {
      recipient: '',
      message: ''
    }
  },
  mounted() {
    this.$store.dispatch('loadMessages')
  },
  methods: {
    sendMessage() {
      this.v$.$validate()
      console.log(this.v$)
      if (!this.v$.$error && confirm('Are you sure you want to send?')) {
        console.log('Confirmed')
        const data = {
          recipient: this.recipient,
          message: this.message,
          sender_username: JSON.parse(window.localStorage.userData).email
        }

        this.$store.dispatch('submitMessage', data).then(() => {
          console.log('dispatched')
          this.$router.push('/messages')
          alert('Message sent successfully')
        })
      } else {
        console.log(this.v$)
        console.log(this.v$.$errors)
      }
    }
  },
  computed: {
    ...mapState(['messages']),
    filteredMessages: function () {
      return this.messages.filter((m) => {
        return m.recipient_username.match(
          JSON.parse(window.localStorage.userData).email
        )
      })
    }
  },
  validations() {
    return {
      recipient: { required },
      message: { required }
    }
  }
}
</script>
<style>
/* Banner */
.image-banner {
  /*Photo by <a href="https://unsplash.com/@ollipexxer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Oliver Pecker</a> on <a href="https://unsplash.com/s/photos/technology?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>*/
  background-image: url(../assets/browse-banner.jpg);
  background-position: center center;
}

.image-banner h1 {
  color: var(--color-highlight);
  font-size: 40px;
}

.image-banner h2 {
  color: var(--color-highlight);
}

.banner-section1 {
  width: 100%;
  margin-bottom: 3em;
}

/* Content */
.content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin: 0 auto;
  padding: 0;
}

.items-container {
  width: 45%;
}

.map-container {
  width: 50%;
  border: 1px solid black;
  margin: 0;
  padding: 0;
}

/* filter */
.filters {
  display: flex;
}
.filter-container {
  display: flex;
  flex-direction: column;
  margin-right: 15px;
}

/* Devices */
/* Devices container */
.devices-container {
  width: 80%;
  border: 1px solid var(--color-primary);
  padding: 4rem 4rem;
  margin: 30px auto;
  border-radius: 5px;
  background-color: var(--color-highlight);
}

.devices-item-container {
  /* position: relative; */
  margin: 0 15px 30px 0;
}

.devices-content {
  width: 100%;
  display: flex;
  align-items: center;
  flex-flow: row wrap;
}

/* Search */
.search-container {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.search-content {
  background-color: var(--color-highlight);
  box-shadow: inset 0 0 0 2000px rgba(62, 124, 177, 0.2);
  width: 80%;
  margin: 30px auto;
  height: 50px;
  border: 1px solid var(--color-pop);
  border-radius: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
  border-radius: 60px;
}
.my-icon {
  width: 30px;
  height: 30px;
}
.search-bar {
  background: transparent;
  outline: none;
  font-size: 20px;
  all: unset;
  width: 100%;
  height: 100%;
  padding: 10px;
}
.search-button {
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  background: transparent;
  margin-right: 10px;
}
</style>
