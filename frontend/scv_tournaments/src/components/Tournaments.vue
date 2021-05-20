<template>
  <div>
    <b-card header-tag="header">
      <template #header>
        <h6 class="mb-0">Seleccionar Torneo</h6>
      </template>
      <b-card-text>
        <b-alert :show="!tournaments.length" variant="secondary">No hay torneos cargados</b-alert>
        <b-list-group>
          <b-list-group-item v-for="t in tournaments" :key="t.id" v-on:click="selectTournament(t.id)" button>
            {{ t.name }}
          </b-list-group-item>
        </b-list-group>
      </b-card-text>
    </b-card>
  </div>
</template>
<script>
export default {
  data() {
    return {}
  },
  methods: {
    selectTournament(id) {
      this.$parent.selectTournament(id);
    }
  },
  props: ['tournaments']
}
</script>