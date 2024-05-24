<script setup lang="ts">
</script>

<template>
  <div>
    <nav>
      <router-link to="/" class="mr-4">Home</router-link>
      <router-link to="/control"> Robô</router-link>
      <router-link to="/about">Registros</router-link>
      <notifications />
    </nav>
    <router-view></router-view>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
