<template>
    <div class="payment">
        <h1>Payment page for customers</h1>
        <stripe-checkout
        ref="checkoutRef"
        mode="payment"
        :pk="publishableKey"
        :line-items="lineItems"
        :success-url="successURL"
        :cancel-url="cancelURL"
        @loading="v =>loading = v"
        />
        
        <button style="position: center;padding:5cm;padding-top: 5cm;margin-top: 3cm;margin-left:10cm" @click="submit" >Pay Now</button>
        
    </div>
    
</template>
<script>
import {StripeCheckout} from '@vue-stripe/vue-stripe'
export default{
    components:{
        StripeCheckout
    },
    data(){
        this.publishableKey="pk_test_51M7SfBKnP1V49iZXCX37ZBvX84DbatoQDyETEarDIQPgci4cnhxPmCLgId4w1zeYWkekCDiioYFaAPSRT94LSoAJ00V5Bdi3PD"
        return{
            loading:false,
            lineItems:[
                {
                    price:'price_1M7SkoKnP1V49iZX2Thvv0Q3',
                    quantity:1
                }
            ],
            successURL:'http://127.0.0.1:5173/success',
            cancelURL:'http://localhost:8080/error'

        }
    },
    methods:{
        submit(){
            this.$refs.checkoutRef.redirectToCheckout()
        }
    }
}
</script>
<style>
.button{
    position:absolute;
    width: 100%;
  bottom: 0;
  padding-bottom: 3in;
  /* border:none;
  margin-left: auto; */
}
</style>