<template>
  <div id="app">
    <Navbar/>
    <ModalTournaments :tournaments="tournaments"/>
    <b-container>
      <b-row class="mt-3">
        <b-col cols="8">
          <div v-for="matchday in matchdays" :key="matchday.id">
            <Matchday :matchday="matchday"/>
          </div>
        </b-col>
        <b-col cols="4">
          <b-table v-if="tournament" small sticky-header striped hover :items="tournament.positions"
                   :fields="['name', 'won', 'lost', 'tie', 'score']"
                   no-border-collapse>
          </b-table>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import ModalTournaments from './components/ModalTournaments.vue';
import Matchday from "./components/Matchday";

const axios = require('axios');

export default {
  name: 'App',
  components: {
    Navbar,
    ModalTournaments,
    Matchday
  },
  data: function () {
    return {
      current_tournament: 1,
      tournaments: [],
      tournament: null,
      matchdays: []
    }
  },
  created: function () {
    axios.get('/backend/api/tournament.json').then(response => {
      this.tournaments = response.data
    })

    axios.get('/backend/api/tournament/' + this.current_tournament + '/', {
      params: {format: 'json',}
    }).then(response => {
      this.tournament = response.data
    })

    axios.get('/backend/api/matchday/', {
      params: {format: 'json', tournament: this.current_tournament}
    }).then(response => {
      this.matchdays = response.data
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
}
</style>
