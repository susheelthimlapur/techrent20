<template lang="">
  <h1>Admin Page</h1>
  <div class="tab">
    <router-link class="tablinks" to="/admin/items">Items</router-link>
    <router-link class="tablinks" to="/admin/complaints"
      >Complaints</router-link
    >
  </div>
  <router-view></router-view>
</template>
<script>
export default {}
</script>
<style scoped>
/* Style the tab */
.tab {
  overflow: hidden;
}

/* Style the buttons that are used to open the tab content */
.tablinks {
  background-color: var(--color-primary);
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  transition: 0.3s;
}

/* Change background color of buttons on hover */
.tablinks:hover {
  background-color: var(--color-pop);
  color: var(--color-primary);
}

/* Create an active/current tablink class */
a.router-link-active.active.tablinks,
.tablinks:focus {
  background-color: var(--color-pop);
  color: var(--color-highlight);
}
</style>
