<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <div class="whitecanna">
      <WhiteCanna />
    </div>
    <div :class="['line', { 'line-collapsed': collapsed }]"></div>
    <div class="nav">
      <button class="nav-button" @click="goToControl">
        <i class="fas fa-signal icon"></i>
        <span v-if="!collapsed">Central de Controle</span>
      </button>
      <button class="nav-button" @click="goToRegister">
        <i class="fas fa-users icon"></i>
        <span v-if="!collapsed">Registro de Uso</span>
      </button>
      <button class="nav-button" @click="goToHome">
        <i class="fas fa-folder-open icon"></i>
        <span v-if="!collapsed">Histórico de Dados</span>
      </button>
      <button v-if="!collapsed" class="out-button" @click="goToLogin">
        <i class="fa-solid fa-right-from-bracket fa-rotate-270"></i>
        <span class="button-text"> Sair </span>
      </button>
    </div>
    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left"></i>
    </span>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { collapsed, sidebarWidth, toggleSidebar } from '../state/state';
import { useRouter } from 'vue-router';
import WhiteCanna from '../assets/whitecanna.svg';

export default defineComponent({
  name: 'SidebarComponent',
  setup() {
    const router = useRouter();

    function goToControl() {
      router.push('/control');
    }

    function goToRegister() {
      router.push('/register');
    }

    function goToHome() {
      router.push('/home');
    }

    function goToLogin(){
      router.push('/login')
    }

    return {
      collapsed,
      toggleSidebar,
      sidebarWidth,
      goToControl,
      goToRegister,
      goToHome,
      goToLogin,
      WhiteCanna
    };
  }
});
</script>

<style>
:root {
  --sidebar-bg-color: #077336;
  --sidebar-item-hover: #C3C1C1;
}
</style>

<style scoped>
.line {
  height: 0.12rem;
  background-color: white;
  align-self: center;
  margin-bottom: 0.4rem;
  transition: width 0.4s ease;
  width: 16rem;
}

.line-collapsed {
  width: 3rem;
}

.sidebar {
  color: #077336;
  background-color: var(--sidebar-bg-color);
  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;
  transition: 0.4s ease;
  display: flex;
  flex-direction: column;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 1.28em;
  color: aliceblue;
  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}
 .out-button{
  color: black;
  border: none;
  background: transparent;
  display: flex;
  align-items: center;
  padding: 0.75em;
  margin: 0.25em ;
  cursor: pointer;
  white-space: nowrap; 
  margin-top: 24em;

 }

 .button-text {
  margin-left: 0.5em;
  font-size: 1.1em;
  font-weight:bold;
}
.nav-button {
  color: white;
  border: none;
  background: transparent;
  display: flex;
  align-items: center;
  padding: 0.75em;
  margin: 0.25em 0;
  cursor: pointer;
  white-space: nowrap; 
}

.nav-button i {
  margin-right: 0.5em;
}

.icon {
  margin: 0.75rem 0.25rem 0.5rem;
}

.whitecanna{
  padding-top: 10;
}

</style>
