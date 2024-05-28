<template>
  <div id="app" class="flex flex-col h-screen overflow-hidden p-4">
    <h1 class="title">Central de Controle</h1>
    <div class="container flex flex-1 overflow-hidden space-x-4">
      <div class="left-half flex-2 flex items-center justify-center bg-gray-200 p-4 border-4">
        <CameraComponent />
      </div>
      <!-- Separa os componentes um em cima do outro -->
      <div class="right-half flex-1 flex flex-col space-y-4">
        <div class="top-half flex-1 flex items-center justify-center border-b border-gray-300 p-4">
          <TeleopComponent />
        </div>
        <div class="bottom-half flex-1 flex items-center justify-center p-4">
          <SensorComponent />
        </div>
      </div>
    </div>
    <div class="flex justify-between p-4 bg-white border-t border-gray-300 mt-4">
      <button class="bg-red-500 text-white py-2 px-4 rounded">
        Modo de Emergência
      </button>
      <button class="bg-green-500 text-white py-2 px-4 rounded">
        Modo Manual
      </button>
    </div>
  </div>
</template>

<script>
import CameraComponent from '../components/CameraComponent.vue'
import TeleopComponent from '../components/TeleopComponent.vue'
import SensorComponent from '../components/SensorComponent.vue'

export default {
  name: 'App',
  components: {
    CameraComponent,
    TeleopComponent,
    SensorComponent
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.title {
  font-family: 'Poppins';
  text-align: left;
  font-size: 2.3rem;
}

.container {
  display: flex;
  height: 100%;
}

.left-half {
  flex: 2;
  display: flex;
  align-items: center;
  justify-content: center;
}

.right-half {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.top-half {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid #ccc;
}

.top-half, .bottom-half {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #ccc;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

</style>
