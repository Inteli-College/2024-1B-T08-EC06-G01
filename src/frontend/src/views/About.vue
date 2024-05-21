<template>
    <div class="container">
        <div class="column">
          <h2 class="title">Registros de Uso</h2>
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
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>rodrigo</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
          <tr>
            <td>rizzi</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
          <tr>
            <td>gustavo</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
          <tr>
            <td>ana</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
          <tr>
            <td>luiz</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
          <tr>
            <td>eduardo</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
          <tr>
            <td>laurA</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
          <tr>
            <td>nicola</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
          <tr>
            <td>murilo</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
          <tr>
            <td>rodrigo</td>
            <td>14/05/24</td>
            <td>14h46</td>
          </tr>
        </tbody>
      </table>
        </div>
    </div>
</template>
  
<script>
  export default {
    name: 'About'
  }

  import { ref } from 'vue';
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
  }

  .checkbox-container input[type="checkbox"]:checked {
  background-color: #17CE67;
  content: '';
  display: inline-block;
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
  