<template>
  <div class="flex justify-between items-center w-full">
    <div class="flex space-x-2">
      <button class="p-2 bg-gray-300 rounded" @click="moveForward">&#9650; Hi</button>
      <button class="p-2 bg-gray-300 rounded">&#9664;</button>
      <button class="p-2 bg-gray-300 rounded">&#9660;</button>
      <button class="p-2 bg-gray-300 rounded">&#9654;</button>
    </div>
    </div>  
  </template>
  
  <script>
  export default {
    name: 'TeleopComponent',
    // Em métodos vocÊ define as funções que serão chamadas no template 
    methods: {
      moveForward() {
        console.log('Moving Forward')
      },
      moveBackward() {
        console.log('Moving Backward')
      },
      moveLeft() {
        console.log('Moving Left')
      },
      moveRight() {
        console.log('Moving Right')
      },

      // As funções abaixo são utilizadas para detectar quando as teclas foram pressionadas 
      handleKeypress(event) {
        if (event.key === 'w' || event.key === 'ArrowUp' || event.key === 'W') {
          this.moveForward()
        }
      
        else if (event.key === 's' || event.key === 'ArrowDown' || event.key === 'S') {
          this.moveBackward()
        }

        else if (event.key === 'a' || event.key === 'ArrowLeft' || event.key === 'A') {
          this.moveLeft()
        }

        else if ( event.key === 'd' || event.key === 'ArrowRight' || event.key === 'D') {
          this.moveRight()
        }
      },
    },
      mounted(){
        window.addEventListener('keydown', this.handleKeypress);
      },
      beforeDestroy(){
        window.removeEventListener('keydown', this.handleKeypress);
      }
    };
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
  