<template>
  <div class="flex justify-center items-center w-full">
    <div class="flex flex-col items-center space-y-2">
      <div>
        <button :class="{ 'clicked': isForwardClicked }"><ArrowUp /></button>
      </div>
      <div class="flex space-x-2">
        <button :class="{ 'clicked': isLeftClicked }"><ArrowLeft /></button>
        <button :class="{ 'clicked': isBackwardClicked }"><ArrowDown /></button>
        <button :class="{ 'clicked': isRightClicked }"><ArrowRight /></button>
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

    // Data é onde você define as variáveis que serão utilizadas no template
    data() {
      return {
        isForwardClicked: false,
        isBackwardClicked: false,
        isLeftClicked: false,
        isRightClicked: false
      }
    },
      

    // Em métodos vocÊ define as funções que serão chamadas no template 
    methods: {
      emergencyStop() {
        console.log('Emergency Stop')
      },
      moveForward() {
        this.isForwardClicked = true;
        console.log('Moving Forward');

      },
      moveBackward() {
        this.isBackwardClicked = true;
        console.log('Moving Backward')
      },
      moveLeft() {
        this.isLeftClicked = true;
        console.log('Moving Left')
      },
      moveRight() {
        this.isRightClicked = true;
        console.log('Moving Right')
      },

      // As funções abaixo são utilizadas para detectar quando as teclas foram pressionadas 
      handleKeypress(event) {
      if (event.key === 'w' || event.key === 'ArrowUp' || event.key === 'W') {
        this.moveForward();
      } else if (event.key === 's' || event.key === 'ArrowDown' || event.key === 'S') {
        this.moveBackward();
      } else if (event.key === 'a' || event.key === 'ArrowLeft' || event.key === 'A') {
        this.moveLeft();
      } else if (event.key === 'd' || event.key === 'ArrowRight' || event.key === 'D') {
        this.moveRight();
      } else if (event.key === 'q' || event.key === 'Q') {
        this.emergencyStop();
      }
    },

    handleKeyup(event) {
      if (event.key === 'w' || event.key === 'ArrowUp' || event.key === 'W') {
        this.isForwardClicked = false;
      }
      else if (event.key === 's' || event.key === 'ArrowDown' || event.key === 'S') {
        this.isBackwardClicked = false;
      }
      else if (event.key === 'a' || event.key === 'ArrowLeft' || event.key === 'A') {
        this.isLeftClicked = false;
      }
      else if (event.key === 'd' || event.key === 'ArrowRight' || event.key === 'D') {
        this.isRightClicked = false;
      }
    }
  },
  
  mounted() {
    window.addEventListener('keydown', this.handleKeypress);
    window.addEventListener('keyup', this.handleKeyup);
  },
  
  beforeDestroy() {
    window.removeEventListener('keydown', this.handleKeypress);
    window.removeEventListener('keyup', this.handleKeyup);
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

  button {
    background-color: transparent;
    border: none;
    cursor: pointer;
  }

  .clicked {
    filter: invert(48%) sepia(79%) saturate(2476%) hue-rotate(86deg) brightness(118%) contrast(119%);
  }



  </style>
  