<template>
        <!-- Temperature Display -->
        <div class="flex items-center">
          <div class="w-20 h-20 bg-gradient-to-r from-green-400 to-yellow-400 rounded-full flex items-center justify-center">
            <span class="text-2xl">45º</span>
          </div>
          <span class="ml-2 text-xl">Temperatura Atual</span>
        </div>
  </template>
  
  <script>
  export default {
    name: 'SensorComponent'
  }
  </script>
  
  <style scoped>
  .bottom {
    background-color: #d4edda;
    height: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
  }
  </style>
  