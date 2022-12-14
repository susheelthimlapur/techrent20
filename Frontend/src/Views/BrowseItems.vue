<template lang="">
  <div class="banner image-banner">
    <div class="banner-container">
      <div class="banner-section1">
        <h1>Browse Electronic Devices</h1>
        <h2>Search, filter, and locate items</h2>
      </div>
    </div>
  </div>
  <div class="content">
    <div class="items-container">
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
        <a
          style="
            position: center;
            margin-top: 3cm;
            margin-left: 10cm;
            right: -10mm;
            bottom: 50px;
          "
          href="/refund"
          type="submit"
          class="request-button"
          >Request a refund</a
        >

        <div class="filters">
          <div class="filter-container">
            <label for="filter-price">Price</label>
            <select
              id="filter-price"
              name="filter-price"
              v-model="selectedPrice"
            >
              <option value="">----</option>
              <option value="low-high">low-high</option>
              <option value="high-low">high-low</option>
            </select>
          </div>
          <div class="filter-container">
            <label for="filter-device-type">Device Type</label>
            <select
              id="filter-device-type"
              name="filter-device-type"
              v-model="selectedType"
            >
              <option value="">----</option>
              <option value="audio">audio</option>
              <option value="video">video</option>
              <option value="computer">computer</option>
              <option value="entertainment">entertainment</option>
            </select>
          </div>
          <div class="filter-container">
            <label for="filter-location">Location</label>
            <select
              id="filter-location"
              name="filter-location"
              v-model="selectedLocation"
            >
              <option value="">----</option>
              <option value="<5miles">5miles</option>
              <option value="10 - 50miles">10 - 50miles</option>
              <option value=">100miles">100miles</option>
            </select>
          </div>
          <div class="filter-container">
            <label for="filter-brand">Brand</label>
            <select
              id="filter-brand"
              name="filter-brand"
              v-model="selectedBrand"
            >
              <option value="">----</option>
              <option value="Apple">Apple</option>
              <option value="Windows">Windows</option>
              <option value="Samsung">Samsung</option>
              <option value="Sony">Sony</option>
              <option value="Bose">Bose</option>
              <option value="Lenovo">Lenovo</option>
            </select>
          </div>
        </div>
      </div>

      <div class="devices-container">
        <div class="devices-header">
          <h2>Searched Items</h2>
          <hr />
        </div>
        <div class="devices-content">
          <div v-for="device in filteredDevices" class="devices-item-container">
            <Recommendation :device="device" class="recommendation" />
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="map-container">
      <h1>PLACEHOLDER MAP</h1>
    </div> -->
  </div>
</template>
<script>
import Recommendation from '@/components/Recommendation.vue'
import { mapState } from 'vuex'
export default {
  components: { Recommendation },
  data() {
    return {
      search: '',
      selectedPrice: '',
      selectedType: '',
      selectedLocation: '',
      selectedBrand: ''
    }
  },
  methods() {},
  computed: {
    filteredDevices: function () {
      return this.items.items
        .filter((device) => {
          return (
            device.item_name.match(this.search) &&
            device.brand.match(this.selectedBrand) &&
            //device.location.match(this.selectedLocation)
            device.item_type.match(this.selectedType)
          )
        })
        .sort((a, b) => {
          if (this.selectedPrice == 'low-high') {
            return a.price - b.price
          } else if (this.selectedPrice == 'high-low') {
            return b.price - a.price
          }
        })
    },
    ...mapState(['items'])
  }
}
</script>
<style scoped>
/* Banner */
.image-banner {
  /*Photo by <a href="https://unsplash.com/@ollipexxer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Oliver Pecker</a> on <a href="https://unsplash.com/s/photos/technology?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>*/
  background-image: url(@/assets/browse-banner.jpg);
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
  align-items: stretch;
  width: 100%;
  margin: 0 auto;
  padding: 0;
}

.items-container {
  width: 100%;
}

.map-container {
  width: 50%;
  border: 1px solid black;
  margin: 0;
  padding: 0;
  background-image: url(@/assets/Mapbox-Google-Maps-API-Alternative-1024x518.png);
  background-position: top center;
  background-repeat: no-repeat;
}

/* Recommendation */
.recommendation {
  height: 300px;
  width: 300px;
}

.recommendation:hover {
  height: 295px;
  width: 295px;
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
  margin: 0 15px 30px 0;
}

.devices-content {
  width: 100%;
  display: flex;
  justify-content: center;
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
