<template>
  <div class="container">
    <div class="column">
      <h2 class="title">Histórico de Dados</h2>
      <p class="subtitle">Último heatmap gerado:</p>
      <div class="line"></div>
      <div class="heatmap"></div>
    </div>
    <div class="column2">
      <div class="dropdown">
        <button class="dropdown-toggle" @click="toggleDropdown">
          {{ selectedOption || 'Ordenar por' }}
          <i class="fas fa-chevron-down" :class="{ 'rotated': isOpen }"></i>
        </button>

        <!-- A lógica dos filtros não está implementada -->
        <div v-if="isOpen" class="dropdown-menu">
          <a href="#" class="dropdown-item" @click.prevent="selectOption('Data')">
            Data <i class="fas" :class="selectedOption === 'Data' ? 'fa-chevron-up' : 'fa-chevron-down'"></i>
          </a>

          <a href="#" class="dropdown-item" @click.prevent="selectOption('Hora')">Data <i class="fas" :class="selectedOption === 'Hora' ? 'fa-chevron-up' : 'fa-chevron-up'"></i></a>

          <a href="#" class="dropdown-item" @click.prevent="selectOption('Localização')">Temperatura <i class="fas" :class="selectedOption === 'Temperatura' ? 'fa-chevron-up' : 'fa-chevron-down'"></i></a> 

          <a href="#" class="dropdown-item" @click.prevent="selectOption('Temperatura')">
            Temperatura <i class="fas" :class="selectedOption === 'Temperatura' ? 'fa-chevron-up' : 'fa-chevron-up'"></i>
          </a>
        </div>
      </div>
      <table class="table">
        <thead>
          <tr>
            <th>Data</th>
            <th>Hora</th>
            <th>Localização</th>
            <th>Temperatura</th>
            <th>Uso de IA</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>01/06/2022</td>
            <td>12:00</td>
            <td>Local A</td>
            <td>25°C</td>
            <td>Sim</td>
          </tr>
          <tr>
            <td>02/06/2022</td>
            <td>13:00</td>
            <td>Local B</td>
            <td>26°C</td>
            <td>Não</td>
          </tr>
          <tr>
            <td>03/06/2022</td>
            <td>14:00</td>
            <td>Local C</td>
            <td>27°C</td>
            <td>Sim</td>
          </tr>
          <tr>
            <td>03/06/2022</td>
            <td>14:00</td>
            <td>Local C</td>
            <td>27°C</td>
            <td>Não</td>
          </tr>
          <tr>
            <td>03/06/2022</td>
            <td>14:00</td>
            <td>Local C</td>
            <td>27°C</td>
            <td>Sim</td>
          </tr>
          <tr>
            <td>03/06/2022</td>
            <td>14:00</td>
            <td>Local C</td>
            <td>27°C</td>
            <td>Não</td>
          </tr>
          <tr>
            <td>03/06/2022</td>
            <td>14:00</td>
            <td>Local C</td>
            <td>27°C</td>
            <td>Sim</td>
          </tr>
          <tr>
            <td>03/06/2022</td>
            <td>14:00</td>
            <td>Local C</td>
            <td>27°C</td>
            <td>Não</td>
          </tr>
          <tr>
            <td>03/06/2022</td>
            <td>14:00</td>
            <td>Local C</td>
            <td>27°C</td>
            <td>Sim</td>
          </tr>
          <tr>
            <td>03/06/2022</td>
            <td>14:00</td>
            <td>Local C</td>
            <td>27°C</td>
            <td>Não</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const isOpen = ref(false);
const selectedOption = ref<string | null>(null);

function toggleDropdown() {
  isOpen.value = !isOpen.value;
}

function selectOption(option: string) {
  selectedOption.value = option;
  isOpen.value = false;
}
</script>

<style scoped>
.container {
  display: flex;
}

.column {
  padding-left: 12rem;
  padding-top: 1rem;
}
.column2 {
  padding-right: 20rem;
  padding-top: 1rem;
  width: 52rem;
}

.title {
  font-family: 'Poppins';
  text-align: left;
  font-size: 2.3rem;
}

.subtitle {
  font-family: 'Public sans';
  text-align: left;
  font-size: 1.25rem;
  padding-top: 1.8rem;
}

.line {
  margin-top: 0.2rem;
  height: 0.16rem;
  width: 13.8rem;
  background-color: #369C62;
}

.heatmap {
  margin-top: 4rem;
  width: 28rem;
  height: 28rem;
  background-image: radial-gradient(circle at center, 
    #FF0000 8%,   /* vermelho */
    #FFA500 30%,  /* laranja */
    #FFFF00 48%,  /* amarelo */
    #008000 70% /* verde */
  );
  border-radius: 50%;
  background-clip: padding-box;
}

.dropdown {
  position: relative;
  display: inline-block;
  padding-top: 6.5rem;
  padding-right: 0.6rem;
  padding-left: 8rem;
}

.dropdown-toggle {
  background-color: #4CDD8B;
  color: black;
  padding: 0.4rem;
  font-size: 0.85rem;
  font-family: Poppins;
  border: none;
  cursor: pointer;
  width: 10.56rem;
  text-align: left;
  padding-left: 0.9rem;
  border-radius: 0.2rem;
  position: relative;
  padding-right: 2rem;
}

.dropdown-toggle i {
  position: absolute;
  top: 50%;
  right: 0.6rem;
  transform: translateY(-50%);
  transition: transform 0.3s;
}

.rotated {
  transform: translateY(-50%) rotate(180deg);
}

.dropdown-menu {
  display: block;
  font-size: 0.85rem;
  font-family: Poppins;
  position: absolute;
  background-color: white;
  min-width: 10rem;
  box-shadow: 0rem 0.5rem 1rem 0rem rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-item {
  color: black;
  padding: 0.75rem 1rem;
  text-decoration: none;
  display: block;
  text-align: left;
  width: 10.56rem;
}

.dropdown-item:nth-child(even) {
  background-color: #E4FFF0; 
}

.dropdown-item:nth-child(odd) {
  background-color: #D1FDE4; 
}

.dropdown-item:hover {
  background-color: #f1f1f1;
}

.dropdown:hover .dropdown-menu,
.dropdown-menu:hover {
  display: block;
}

.table {
  margin-left: 8rem;
  width: 44rem;
  border-collapse: collapse;
  margin-top: 4rem;
  cursor: pointer;
}

.table th, .table td {
  border: 0.06rem solid;
  padding: 0.5rem;
  padding-left: 1rem;
  padding-right: 1rem;
  text-align: center;
  font-family: Poppins;
  font-weight: normal;
}

.table th {
  background-color: #ffffff;
}

.table tbody tr:nth-child(even) {
  background-color: #ffffff;
}

.table tbody tr:hover {
  background-color: #E4FFF0;
}

.table tbody tr:nth-child(odd) {
  height: 1.8rem;
}

.table tbody tr:nth-child(even) {
  height: 1.8rem;
}

</style>