<template>
  <div id="app" class="flex flex-col h-screen overflow-hidden p-4">
    <h1 class="title mb-8">Central de Controle</h1>
    <div class="container flex flex-1 overflow-hidden space-x-4 pl-4"> <!-- Ajuste de padding-left aqui -->
      <div class="left-half flex-2 flex items-center justify-center p-4">
        <CameraComponent />
      </div>
      <div class="right-half flex-1 flex flex-col space-y-4">
        <div class="top-half flex-1 flex items-center justify-center p-4">
          <TeleopComponent />
        </div>
        <div class="bottom-half flex-1 flex items-center justify-center p-4">
          <SensorComponent />
        </div>
      </div>
    </div>
    <div class="flex p-4 bg-white border-gray-300 mt-4 ml-40"> <!-- Removi a classe border-t -->
      <button class="bg-red-500 text-white py-2 px-8 rounded">
        Modo de Emergência
      </button>
      <div class="flex-grow"></div>
      <button class="bg-green-600 text-white py-2 px-8 rounded mr-12">
        Verificação de Resíduos
      </button>
      <button class="bg-green-500 text-white py-2 px-4 rounded mr-12">
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
  padding-left: 11rem;
}

.container {
  display: flex;
  height: 100%;
  padding-left: 9rem;
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

.top-half, .bottom-half {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #fff;
}
</style>
