<template>
  <div id="app">
    <h1 class="title">Central de controle</h1>
    <div class="container">
      <div class="left-half">
        <CameraComponent />
      </div>
      <div class="right-half">
        <div class="top-half">
          <TeleopComponent />
        </div>
        <div class="bottom-half">
          <SensorComponent />
        </div>
      </div>
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

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.title {
  font-size: 36px;
  margin-bottom: 10px;
}

.container {
  display: flex;
  height: 100vh;
  padding: 0 20px;
  box-sizing: border-box;
}

.left-half {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid #ccc;
}

.right-half {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.top-half, .bottom-half {
  flex: 1;
  border-bottom: 1px solid #ccc;
}

.bottom-half {
  border-bottom: none;
}
</style>
