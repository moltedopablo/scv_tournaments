<template>
  <div id="app">
    <Navbar/>

    <b-container>
      <h3 v-if="tournament" class="mt-3 mb-2 text-left">Torneo: {{tournament.name}}</h3>
      <b-row class="mt-3 text-left">
        <b-col cols="8">
          <div v-if="tournament">
            <div v-for="matchday in matchdays" :key="matchday.id">
              <Matchday :matchday="matchday"/>
            </div>
          </div>
          <div v-else>
            <Tournaments v-if="tournaments.length" :tournaments="tournaments"/>
            <TournamentForm />
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
import Tournaments from './components/Tournaments.vue';
import Matchday from "./components/Matchday.vue";
import TournamentForm from "./components/TournamentForm.vue";

const axios = require('axios');

export default {
  name: 'App',
  components: {
    Navbar,
    Tournaments,
    Matchday,
    TournamentForm
  },
  data: function () {
    return {
      current_tournament: null,
      tournaments: [],
      tournament: null,
      matchdays: []
    }
  },
  methods: {
    selectTournament(id) {
      this.current_tournament = id
      this.fetchTournament()
      this.fetchMatchdays()
    },
    fetchTournaments() {
      axios.get('/backend/api/tournament.json').then(response => {
        this.tournaments = response.data
      })
    },
    fetchTournament() {
      axios.get('/backend/api/tournament/' + this.current_tournament + '/', {
        params: {format: 'json',}
      }).then(response => {
        this.tournament = response.data
      })
    },
    fetchMatchdays() {
      axios.get('/backend/api/matchday/', {
        params: {format: 'json', tournament: this.current_tournament}
      }).then(response => {
        this.matchdays = response.data
      })
    }
  },
  created: function () {
    this.fetchTournaments()
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
