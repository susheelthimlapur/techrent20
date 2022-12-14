<template lang="">
  <div class="container">
    <h2>Are you sure you want to log out?</h2>
    <div class="buttons">
      <button>Yes</button>
      <button>No</button>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style scoped>
.container {
  top: 250px;
  width: 30%;
  height: auto;
  padding: 10px;
  border: 1px solid black;
  background: var(--color-highlight);
  z-index: 100000000;
}

.buttons {
  display: flex;
  align-items: center;
  justify-content: space-around;
}

button {
  width: 30%;
}
</style>
