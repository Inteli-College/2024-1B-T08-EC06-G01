<template>
  <div class="flex justify-between items-center w-full">
    <div class="flex space-x-2">
      <button class="p-2 bg-gray-300 rounded">&#9650;</button>
      <button class="p-2 bg-gray-300 rounded">&#9664;</button>
      <button class="p-2 bg-gray-300 rounded">&#9660;</button>
      <button class="p-2 bg-gray-300 rounded">&#9654;</button>
    </div>
    </div>  
  </template>
  
  <script>
  export default {
    name: 'TeleopComponent'
  }
  </script>
  
  <style scoped>
  .top {
    background-color: #cce5ff;
    height: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
  }
  </style>
  