<template lang="">
  <div class="banner image-banner">
    <div class="banner-container">

        <!-- <div class="image-container">
          <h1>PLACEHOLDER Image</h1>
        </div> -->
      </div>
    </div>
      <div class="content">
        <div class="items-container">
          <div class="info-container">
            <div class="info-content" v-for="i in item">
              <h1 class="item-content1">Product Info</h1>
              <br />
              <!-- <h2> Product Name: {{aitemname}}</h2><br><br/> -->
              <img
                src="../assets/taperecorder.jpg"
                style="width: 200px; left: 300px"
              />
              <h2 class="item-content2" style="top: -35px; right: 45px">
                Product Name: {{ i.item_name }}
              </h2>
              <br />
              <h2 class="item-content3" style="top: 15px; right: 400px">
                Price: $20 {{ i.price }}
              </h2>
              <br />
              <h2 class="item-content4" style="top: 20px; right: 61px">
                Brand: Sony{{ i.brand }}
              </h2>
              <br />
              <!-- <h2 > Brand: {{aitembrand}}</h2><br></br> -->
              <h2 class="item-content5" style="top: 20px; right: 39px">
                Location: Bloomington{{ i.location }}
              </h2>
              <br />
            </div>
          </div>
        </div>
        <div class="payment">
          <stripe-checkout
            ref="checkoutRef"
            mode="payment"
            :pk="publishableKey"
            :line-items="lineItems"
            :success-url="successURL"
            :cancel-url="cancelURL"
            @loading="(v) => (loading = v)"
          />

          <button
            style="
              position: center;
              margin-top: 3cm;
              margin-left: 10cm;
              right: 850px;
              top: 120px;
            "
            type="submit"
            class=""
            id="payment_button"
            @click="submit"
          >
            Purchase
          </button>
        </div>
  </div>
</template>
<script>
import Recommendation from '@/components/Recommendation.vue'
import { StripeCheckout } from '@vue-stripe/vue-stripe'
import { mapState } from 'vuex'
export default {
  props: [
    'aitemimage',
    'aitemname',
    'aitemtype',
    'aitembrand',
    'aitemlocation',
    'aitemprice'
  ],
  data() {
    this.publishableKey =
      'pk_test_51M7SfBKnP1V49iZXCX37ZBvX84DbatoQDyETEarDIQPgci4cnhxPmCLgId4w1zeYWkekCDiioYFaAPSRT94LSoAJ00V5Bdi3PD'
    return {
      itemId: this.$route.params.id,
      loading: false,
      lineItems: [
        {
          price: 'price_1M7SkoKnP1V49iZX2Thvv0Q3',
          quantity: 1
        }
      ],
      successURL: 'http://127.0.0.1:5173/success',
      cancelURL: 'http://localhost:8080/error'
    }
  },
  components: {
    StripeCheckout
  },
  methods: {
    submit() {
      this.$refs.checkoutRef.redirectToCheckout()
    },
    routeToConfirmation() {
      this.$router.push('/confirmation')
    }
  },
  computed: {
    item: function () {
      console.log(this.items.items, 'id = ' + this.itemId)
      return this.items.items.filter((device) => {
        return device.id == this.itemId
      })
    },
    ...mapState(['items'])
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

/* Devices */
/* Devices container */

.info-item-container {
  /* position: relative; */
  margin: 0 15px 30px 0;
}

.info-content {
  width: 100%;
  display: flex;
  align-items: center;
  flex-flow: row wrap;
}

.info-container {
  width: 150%;
  left: 35px;
  border: 1px solid var(--color-primary);
  padding: 4rem 4rem;
  margin: 30px auto;
  border-radius: 5px;
  background-color: var(--color-highlight);
}

.info-item-container {
  /* position: relative; */
  margin: 0 15px 30px 0;
}

.paymentinfo-content {
  width: 100%;
  display: flex;
  align-items: center;
  flex-flow: row wrap;
}
.paymentinfo-container {
  width: 150%;
  right: 90%;
  top: 300px;
  border: 1px solid var(--color-primary);
  padding: 4rem 4rem;
  margin: 30px auto;
  border-radius: 5px;
  background-color: var(--color-highlight);
  display: flex;
}
.item-content1 {
  display: flex;
  top: -60px;
  justify-content: space-between;
}
.item-content2 {
  left: -440px;
  top: 50px;
  display: flex;
  justify-content: space-between;
}
.item-content3 {
  left: -440px;
  display: flex;
  justify-content: space-between;
}
.item-content4 {
  left: -150px;
  top: -50px;
  display: flex;
  justify-content: space-between;
}
.item-content5 {
  left: -50px;
  top: -100px;
  display: flex;
  justify-content: space-between;
}
</style>
