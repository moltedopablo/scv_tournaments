<template>
  <b-card
      :header="'Fecha ' + matchday.number"
      class="mb-2"
      align="left"
  >
    <b-card-text>
      <b-table-lite small sticky-header striped hover :items="matches"
               :fields="['home_team.name', 'away_team.name', 'home_goals', 'away_goals']" show-empty
               :empty-text="'No tournaments'"
               no-border-collapse>
      </b-table-lite>
    </b-card-text>

  </b-card>
</template>
<script>
const axios = require('axios');

export default {
  data() {
    return {
      matches: null
    }
  },
  created() {
    this.fetchMatches()
  },
  methods: {
    fetchMatches() {
      axios.get('/backend/api/match/', {
        params: {format: 'json', matchday: this.matchday.id}
      }).then(response => {
        this.matches = response.data
      })
    }
  },
  props: ['matchday']
}
</script>