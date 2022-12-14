<template lang="">
  <div class="flex-table">
    <div>Name</div>
    <div>Email</div>
    <div>Description</div>
    <div>Actions</div>
  </div>
  <div class="flex-table">
    <div></div>
    <div></div>
    <div></div>
    <div class="actions">
      <button>Send to renter</button>
      <button @click="refund()">Refund</button>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    refund() {}
  }
}
</script>
<style scoped>
.flex-table {
  display: grid;
  grid-template-columns: repeat(auto-fill, 25%);
  padding: 10px;
  border-bottom: 1px black solid;
}
</style>
