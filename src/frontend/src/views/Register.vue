<template>
  <div class="container">
    <div class="column">
      <h2 class="title">Registros de Uso</h2>

      <!-- A lógica do filtro não está implementada -->
      <div class="checkbox-container">
        <input type="checkbox" id="checkbox" v-model="isChecked">
        <label for="checkbox">Agrupar por usuário</label>
      </div>
      <table class="table">
        <thead>
          <tr>
            <th>Usuário</th>
            <th>Data</th>
            <th>Horário</th>
            <th>Uso do Botão de Emergência</th>
            <th>Requisição da IA</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>rodrigo</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Sim</td>
            <td>Não</td>
          </tr>
          <tr>
            <td>rizzi</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Não</td>
            <td>Sim</td>
          </tr>
          <tr>
            <td>gustavo</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Sim</td>
            <td>Não</td>
          </tr>
          <tr>
            <td>ana</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Não</td>
            <td>Sim</td>
          </tr>
          <tr>
            <td>luiz</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Sim</td>
            <td>Não</td>
          </tr>
          <tr>
            <td>eduardo</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Não</td>
            <td>Sim</td>
          </tr>
          <tr>
            <td>laurA</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Sim</td>
            <td>Não</td>
          </tr>
          <tr>
            <td>nicola</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Não</td>
            <td>Sim</td>
          </tr>
          <tr>
            <td>murilo</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Sim</td>
            <td>Não</td>
          </tr>
          <tr>
            <td>rodrigo</td>
            <td>14/05/24</td>
            <td>14h46</td>
            <td>Não</td>
            <td>Sim</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import { ref } from 'vue';

  export default {
    name: 'Register',
    setup() {
      const isChecked = ref(false);
      return {
        isChecked,
      };
    }
  };
</script>

<style scoped>
  .container {
    display: flex;
  }

  .column {
    padding-left: 12rem;
    padding-top: 1rem;
  }

  .title {
    font-family: 'Poppins';
    text-align: left;
    font-size: 2.3rem;
  }

  .checkbox-container {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    margin-top: 1.8rem;
  }

  .checkbox-container input[type="checkbox"] {
    margin-right: 1.6rem;
    width: 1.1rem;
    height: 1.1rem;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border: 1px solid black;
    position: relative;
  }

  .checkbox-container input[type="checkbox"]::before {
    content: "";
    position: absolute;
    width: 1rem;
    height: 1rem;
    background: #17CE67;
    display: none;
    justify-content: center;
    align-items: center;
    font-size: 0.8rem;
  }

  .checkbox-container input[type="checkbox"]:checked::before {
    display: flex;
    content: "\2713";
    color: white;
  }

  .table {
    width: 80rem;
    border-collapse: collapse;
    margin-top: 4rem;
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
