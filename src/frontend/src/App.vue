<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div>
    <nav class="p-4 bg-gray-200">
      <router-link to="/" class="mr-4">Home</router-link>
      
      <router-link to="/control"> Robô</router-link>

      <router-link to="/about">About</router-link>

    </nav>
  </div>
</template>

<style scoped>
</style>
