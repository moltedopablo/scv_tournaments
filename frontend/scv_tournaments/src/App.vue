<template>
  <div id="app">
    <h2 class="mt-4">Tournaments</h2>
    <b-table small sticky-header striped hover :items="tournaments"
             :fields="['name']" show-empty :empty-text="'No tournaments'"
             no-border-collapse>
    </b-table>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

const axios = require('axios');

export default {
  name: 'App',
  components: {
    // HelloWorld
  },
  data: function () {
    return {
      tournaments: [],
    }
  },
  created: function () {
    axios.get('/backend/api/tournament.json').then(response => {
      this.tournaments = response.data
    })
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
</style>
