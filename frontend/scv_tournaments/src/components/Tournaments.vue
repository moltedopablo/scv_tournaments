<template>
  <div>
    <b-card no-body header-tag="header">
      <template #header>
        <h6 class="mb-0">Seleccionar Torneo</h6>
      </template>
      <b-list-group flush>
        <b-list-group-item v-for="t in tournaments" :key="t.id" v-on:click="selectTournament(t.id)" button>
          {{ t.name }}
        </b-list-group-item>
      </b-list-group>
      <b-card-body>
        <span class="mt-3 p-3" v-if="!tournaments.length">No hay torneos cargados</span>
      </b-card-body>
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