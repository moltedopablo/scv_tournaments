<template>
  <div id="app">
    <Navbar/>
    <b-container>
      <h3 v-if="tournament" class="mt-3 mb-2 text-left">Torneo: {{ tournament.name }}</h3>
      <b-row v-if="tournament" class="mt-3 text-left">
        <b-col lg="7">
          <div v-for="matchday in matchdays" :key="matchday.id">
            <Matchday :matchday="matchday"/>
          </div>
        </b-col>
        <b-col lg="5">
          <Positions v-if="tournament" :positions="tournament.positions"/>
        </b-col>
      </b-row>
      <b-row v-if="!tournament" class="mt-3 text-left">
        <b-col lg="8" class="mb-3">
          <Tournaments :tournaments="tournaments"/>
        </b-col>
        <b-col lg="4">
          <TournamentForm/>
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
import Positions from "./components/Positions.vue";

const axios = require('axios');

export default {
  name: 'App',
  components: {
    Navbar,
    Tournaments,
    Matchday,
    TournamentForm,
    Positions
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
    resetTournament() {
      this.current_tournament = null
      this.tournament = null
      this.fetchTournaments()
    },
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
