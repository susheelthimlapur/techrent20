<!-- eslint-disable vue/multi-word-component-names -->
<template lang="">
  <div class="banner image-banner">
    <div class="banner-container">
      <div class="banner-section1">
        <h1>Electronic Device Rental</h1>
        <h2>A new way to try out that device you have been longing to buy</h2>
      </div>
    </div>
  </div>

  <div class="search-container">
    <form action="" class="search-content">
      <input
        class="search-bar"
        type="text"
        v-model="search"
        placeholder="Search For Electronic Devices"
      />
      <button type="submit" class="search-button">
        <img src="../assets/search.png" class="my-icon" />
      </button>
    </form>
  </div>

  <div v-if="search" class="devices-container">
    <div class="devices-header">
      <h2>Searched Items</h2>
    </div>
    <div class="devices-content">
      <div v-for="device in filteredDevices" class="devices-item-container">
        <Recommendation :device="device" class="recommendation" />
      </div>
    </div>
  </div>

  <div class="recommendations-container">
    <div class="recommendations-header">
      <h2>Recommended Items</h2>
    </div>
    <div class="recommendations-content">
      <div
        v-for="device in recommendedDevices"
        class="recommendations-item-container"
      >
        <Recommendation :device="device" class="recommendation" />
      </div>
    </div>
  </div>
</template>

<script>
import Recommendation from './Recommendation.vue'
import { mapState } from 'vuex'

export default {
  components: { Recommendation },
  data() {
    return {
      recommendedDevices: [],
      search: ''
    }
  },
  methods() {},
  created() {
    // get request
    /*
    .then(function(data){
      this.recommendedDevices = data.body.slice(0,10);
      this.devices = data.body
    })
    */
  },
  computed: {
    recommendedDevices: function () {
      return this.items.items.slice(0, 10)
    },
    filteredDevices: function () {
      console.log(this.items.items)
      return this.items.items.filter((device) => {
        return device.item_name.match(this.search)
      })
    },
    ...mapState(['items'])
  }
}
</script>

<style scoped>
/* Banner */
.image-banner {
  /* Photo by Photo by <a href="https://unsplash.com/@marvelous?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Marvin Meyer</a> on <a href="https://unsplash.com/s/photos/technology?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> */
  background-image: url(../assets/home-banner.jpg);
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

/* Recomendations container */
.recommendations-container {
  width: 80%;
  border: 1px solid var(--color-primary);
  padding: 4rem 4rem;
  margin: 30px auto;
  border-radius: 5px;
  background: var(--color-highlight);
}

.recommendations-item-container {
  /* position: relative; */
  margin: 0 15px 30px 0;
}

.recommendations-content {
  width: 100%;
  display: flex;
  align-items: center;
  flex-flow: row wrap;
}

.recommendations-header {
  text-align: left;
}

/* Search */
.search-container {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
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

/* Medium devices (tablets, 768px and up) */
@media (min-width: 768px) {
  .image-banner {
    background-position: bottom;
  }
}
</style>
