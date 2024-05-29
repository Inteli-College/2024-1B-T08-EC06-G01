<template>
    <div :class="sidebarOpen ? 'translate-x-0' : '-translate-x-full' + ' bg-gray-200 w-64 h-full fixed top-0 left-0 transition-transform duration-300 ease-in-out transform z-10'">
      <div class="p-4">
        <ul v-show="sidebarOpen">
          <li><i class="fa fa-home"></i></li>
          <li><i class="fa fa-user"></i></li>
          <li><i class="fa fa-cog"></i></li>
        </ul>
      </div>
    </div>
  </template>

  <script setup lang="ts">
  import { defineProps, defineEmits } from 'vue';

  defineProps({
    sidebarOpen: Boolean
  });

  defineEmits();

  // const toggleSidebar = () => {
  //   emit('toggle-sidebar');
  // }
  </script>

  <style scoped>
  .translate-x-0 {
    transform: translateX(0);
  }
  .-translate-x-full {
    transform: translateX(-100%);
  }

  .bg-gray-200 {
    background-color: #077336;
  }

  .w-64 {
    width: 16rem;
  }

  .h-full {
    height: 100%;
  }

  .fixed {
    position: fixed;
  }

  .top-0 {
    top: 0;
  }

  .left-0 {
    left: 0;
  }

  .p-4 {
    padding: 1rem;
  }

  .transition-transform {
    transition-property: transform;
  }

  .duration-300 {
    transition-duration: 300ms;
  }

  .ease-in-out {
    transition-timing-function: ease-in-out;
  }

  .transform {
    will-change: transform;
  }

  .z-10 {
    z-index: 10;
  }

  .fa {
    margin-right: 1rem;
  }
  </style>
