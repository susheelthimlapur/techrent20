<template lang="">
  <div class="flex-table">
    <div>Name</div>
    <div>Email</div>
    <div>Description</div>
    <div>Actions</div>
  </div>
  <div v-for="complaint in complaints" :key="complaint.id" class="flex-table">
    <div>{{ complaint.userName }}</div>
    <div>{{ complaint.userEmail }}</div>
    <div>{{ complaint.description.slice(0, 50) + '...' }}</div>
    <div class="actions">
      <!-- <router-link :to="{ name: 'Complaint', params: { id: complaint.id } }">View</router-link> -->
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      complaints: [
        {
          id: 1,
          userName: 'Jim Beam',
          userEmail: 'fake@fake.com',
          description:
            'This is a long complaint it consists of many mnay many words and many many many and many many manyand many many many and many many many and many many many and many many many and many many many'
        },
        {
          id: 2,
          userName: 'Jim Beam',
          userEmail: 'fake@fake.com',
          description:
            'This is a long complaint it consists of many mnay many words and many many many and many many manyand many many many and many many many and many many many and many many many and many many many'
        },
        {
          id: 3,
          userName: 'Jim Beam',
          userEmail: 'fake@fake.com',
          description:
            'This is a long complaint it consists of many mnay many words and many many many and many many manyand many many many and many many many and many many many and many many many and many many many'
        },
        {
          id: 4,
          userName: 'Jim Beam',
          userEmail: 'fake@fake.com',
          description:
            'This is a long complaint it consists of many mnay many words and many many many and many many manyand many many many and many many many and many many many and many many many and many many many'
        }
      ]
    }
  }
  //   computed: {
  //     ...mapState(['userComplaints'])
  //   }
}
</script>
<style scoped>
.flex-table {
  display: grid;
  grid-template-columns: repeat(auto-fill, 25%);
  padding: 10px;
  border-bottom: 1px black solid;
  /* &:nth-of-type(2n) {
    background-color: #dedede;
  } */
}
</style>
