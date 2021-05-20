<template>
  <b-card
      :header="'Fecha ' + matchday.number"
      class="mb-4"
      align="left"
      no-body
  >
    <div class="p-3">
      <b-table-lite table-class="table-responsive-sm" small striped hover :items="matches"
                    :fields="[{key:'home_team.name', label:'Local', class: 'teams_column'},
                   {key:'away_team.name', label:'Visitante',class: 'teams_column'},
                    {key:'home_goals_input', label:'Goles Local', class: 'goals_column'},
                     {key:'away_goals_input', label:'Goles Visitante', class: 'goals_column',},
                     {key:'save', label:''}]"
                    show-empty
                    :empty-text="'No tournaments'"
                    no-border-collapse>
        <template #cell(home_goals_input)="data">
          <b-form-input type="number" v-model="data.item.home_goals" :state="validateGoal(data.item.home_goals)" min="0"
                        step="1"
                        class="numberinput form-control"></b-form-input>
        </template>
        <template #cell(away_goals_input)="data">
          <b-form-input type="number" v-model="data.item.away_goals" :state="validateGoal(data.item.away_goals)" min="0"
                        step="1"
                        class="numberinput form-control"></b-form-input>
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
    validateGoal(number) {
      if (!number || number >= 0) {
        return null
      } else {
        return false
      }
    },
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
@media only screen and (min-width: 600px) {
  .goals_column {
    max-width: 20%;
  }

  .teams_column {
    width: 30%;
  }
}
@media only screen and (max-width: 600px) {
  .goals_column {
    min-width: 98px;
  }
}

</style>