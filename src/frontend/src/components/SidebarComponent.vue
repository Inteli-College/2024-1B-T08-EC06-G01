<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
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

export default defineComponent({
  name: 'SidebarComponent',
  setup() {
    return {
      collapsed,
      toggleSidebar,
      sidebarWidth
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
  transition: 0.3s ease;
  display: flex;
  flex-direction: column;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;
  color: aliceblue;
  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}
</style>
