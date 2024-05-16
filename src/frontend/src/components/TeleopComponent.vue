<template>
  <div class="flex justify-center items-center w-full">
    <div class="flex flex-col items-center space-y-2">
      <div>
        <button @click="moveForward" ><ArrowUp /></button>
      </div>
      <div class="flex space-x-2">
        <button @click="moveLeft" ><ArrowLeft /></button>
        <button @click="moveBackward" ><ArrowDown /></button>
        <button @click="moveRight"><ArrowRight /></button>
      </div>
    </div>
  </div>  
</template>
  
  <script>
  // Importando o SVG das setinhas 
  import ArrowUp from '../assets/arrow-up.svg';
  import ArrowDown from '../assets/arrow-down.svg';
  import ArrowRight from '../assets/arrow-right.svg';
  import ArrowLeft from '../assets/arrow-left.svg';




  export default {
    name: 'TeleopComponent',

    // Adicionando o SVG das setinhas ao componente
    components: {
      ArrowUp,
      ArrowDown,
      ArrowRight,
      ArrowLeft
    },
      

    // Em métodos vocÊ define as funções que serão chamadas no template 
    methods: {
      emergencyStop() {
        console.log('Emergency Stop')
      },
      moveForward() {
        console.log('Moving Forward');
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
        else if ( event.key === 'q' || event.key === 'Q') {
          this.emergencyStop()
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
  