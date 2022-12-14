<template>
  <div class="flex-table">
    <div>Name</div>
    <div>Description</div>
    <div>Actions</div>
  </div>
  <div v-for="item in items.items" :key="item.id" class="flex-table">
    <div>{{ item.item_name }}</div>
    <div>{{ item.description.slice(0, 50) + '...' }}</div>
    <div class="actions">
      <router-link :to="{ name: 'ItemPage', params: { id: item.id } }"
        >Review</router-link
      >
      <button @click="deleteItem(item)">Remove</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data() {
    return {}
  },
  computed: {
    ...mapState(['items'])
  },
  methods: {
    deleteItem(item) {
      let response = confirm(`Are you sure you want to delete ${item.name}`)
      if (response) {
        this.$store.dispatch('deleteItem', item)
      }
    }
  }
}
</script>

<style scoped>
.flex-table {
  display: grid;
  grid-template-columns: repeat(auto-fill, 33%);
  padding: 10px;
  border-bottom: 1px black solid;
  /* &:nth-of-type(2n) {
    background-color: #dedede;
  } */
}
/* 
.actions {
    * {
      padding-right: 15px;
    }
  } */
</style>
