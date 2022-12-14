<template>
  <div class="greetings">
    <h1 class="logo">
      <a href="https://github.com/cam-line/TechRent">{{ msg }}</a>
    </h1>
  </div>
</template>

<script>
export default {
  name: "LogoLink",
  props: {
    msg: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
h1,
a {
  font-weight: 500;
  font-size: 2.6rem;
  color: var(--color-background);
  margin: 0;
  padding: 0;
}

a:hover {
  color: var(--color-highlight);
  padding: 0;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
