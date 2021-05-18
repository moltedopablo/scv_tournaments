<template>
  <b-card
      :header="'Fecha ' + matchday.number"
      class="mb-4"
      align="left"
      no-body
  >

    <b-table-lite small sticky-header striped hover :items="matches"
                  :fields="['home_team.name', 'away_team.name', 'home_goals_input', 'away_goals_input', 'save']"
                  show-empty
                  :empty-text="'No tournaments'"
                  no-border-collapse>
      <template #cell(home_goals_input)="data">
        <input type="number" v-model="data.item.home_goals" step="1"
               class="numberinput form-control">
      </template>
      <template #cell(away_goals_input)="data">
        <input type="number" v-model="data.item.away_goals" step="1"
               class="numberinput form-control">
      </template>
      <template #cell(save)="data">
        <button class="btn btn-sm btn-danger"
                v-on:click="save(data.item)">Guardar
        </button>
      </template>
    </b-table-lite>

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
    },
    save(item) {
      axios.put('/backend/api/match/' + item.id + '/', {home_goals: item.home_goals, away_goals: item.away_goals}, {
        params: {
          format: 'json',
        }
      }).then(() => {
        this.$parent.fetchTournament();
      })
    }
  },
  props: ['matchday']
}
</script>