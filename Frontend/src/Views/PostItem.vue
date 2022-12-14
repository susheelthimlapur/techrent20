<template lang="">
  <div class="post-item">
    <div class="post-item-container">
      <form @submit.prevent="postItem">
        <h1 class="">Post Item</h1>
        <div class="or">
          <h4>Details</h4>
          <hr />
        </div>
        <div class="input">
          <label for="name">Item Name</label>
          <input
            class="form-input"
            type="text"
            name="name"
            v-model="item_name"
            placeholder="name of item you are renting out"
          />
          <div
            class="error"
            v-for="(error, index) of v$.item_name.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>

        <div class="input">
          <label for="brand">Description</label>
          <textarea
            class="form-input"
            type="textarea"
            name="brand"
            v-model="description"
            placeholder="brief description of item and additional details"
          ></textarea>
          <div
            class="error"
            v-for="(error, index) of v$.description.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="filter-brand">Brand</label>
          <select id="filter-brand" name="filter-brand" v-model="brand">
            <option value="">----</option>
            <option value="Apple">Apple</option>
            <option value="Windows">Windows</option>
            <option value="Samsung">Samsung</option>
            <option value="Sony">Sony</option>
            <option value="Bose">Bose</option>
            <option value="Lenovo">Lenovo</option>
          </select>
          <div
            class="error"
            v-for="(error, index) of v$.brand.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="price">Price</label>
          <input
            class="form-input"
            type="number"
            name="price"
            v-model="price"
            placeholder="price to rent item (per day)"
          />
          <div
            class="error"
            v-for="(error, index) of v$.price.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="filter-device-type">Device Type</label>
          <select
            id="filter-device-type"
            name="filter-device-type"
            v-model="item_type"
          >
            <option value="">----</option>
            <option value="audio">audio</option>
            <option value="video">video</option>
            <option value="computer">computer</option>
            <option value="entertainment">entertainment</option>
          </select>
        </div>
        <div class="input">
          <label for="price">Location</label>
          <input
            class="form-input"
            type="text"
            name="location"
            v-model="location"
            placeholder="address to pick up item from"
          />
          <div
            class="error"
            v-for="(error, index) of v$.location.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="item-image">Image</label>
          <input
            class="form-input"
            type="file"
            name="item-image"
            ref="file"
            v-on:change="selectImage"
            accept="image/*"
          />
        </div>
        <div class="or">
          <h4>Contact</h4>
          <hr />
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
          <div
            class="error"
            v-for="(error, index) of v$.email.$errors"
            :key="index"
          >
            {{ error.$message }}
          </div>
        </div>
        <div class="input">
          <label for="phone">Phone Number</label>
          <input
            class="form-input"
            type="text"
            name="phone"
            v-model="phone"
            placeholder="###-###-####"
          />
        </div>
        <button type="submit" class="" id="register_button">
          Post to Website
        </button>
      </form>
    </div>
  </div>
</template>
<script>
import { email, required } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'
export default {
  name: 'RegisterUser',
  setup() {
    return { v$: useVuelidate() }
  },
  data() {
    return {
      item_name: '',
      description: '',
      brand: '',
      item_type: '',
      price: 0,
      location: '',
      image_url: '',
      email: '',
      phone: ''
    }
  },
  methods: {
    postItem() {
      this.v$.$validate()
      console.log(this.v$)
      if (!this.v$.$error && confirm('Are you sure you want to post?')) {
        const data = {
          item_name: this.item_name,
          description: this.description,
          brand: this.brand,
          item_type: this.item_type,
          seller_id: JSON.parse(window.localStorage.userData).uid,
          price: this.price,
          location: this.location,
          image_url: this.image_url,
          email: this.email,
          phone: this.phone
        }
        console.log(data)

        this.$store.dispatch('submitNewItem', data).then(() => {
          console.log('Data image: ' + data.image_url)
          this.$router.push('/browse')
          alert('Form submitted successfully')
        })
      } else {
        console.log(this.v$)
        console.log(this.v$.$errors)
      }
    },
    selectImage() {
      this.image_url = URL.createObjectURL(this.$refs.file.files.item(0))
      // this.previewImage = URL.createObjectURL(this.currentImage);
    }
  },
  validations() {
    return {
      item_name: { required },
      description: { required },
      brand: { required },
      price: { required },
      location: { required },
      email: { required, email }
    }
  }
}
</script>
<style scoped>
.post-item-container {
  width: 80%;
  margin: 25px auto;
  padding: 2em;
  border: 3px solid var(--color-primary);
  border-radius: 8px;
}

.error {
  color: red;
}
</style>
