<template>
  <b-card
      :header="'Fecha ' + matchday.number"
      class="mb-4"
      align="left"
      no-body
  >
    <div class="p-3">
      <b-table-lite small striped hover :items="matches"
                    :fields="[{key:'home_team.name', label:'Local', class: 'teams_column'},
                   {key:'away_team.name', label:'Visitante',class: 'teams_column'},
                    {key:'home_goals_input', label:'', class: 'goals_column'},
                     {key:'away_goals_input', label:'', class: 'goals_column',},
                     {key:'save', label:''}]"
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
          <button class="btn btn-sm btn-primary"
                  v-on:click="save(data.item)">
            <b-icon icon="upload"></b-icon>
          </button>
        </template>
      </b-table-lite>
    </div>
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
<style>
.goals_column {
  max-width: 15%;
}
.teams_column {
  width: 35%;
}
</style>