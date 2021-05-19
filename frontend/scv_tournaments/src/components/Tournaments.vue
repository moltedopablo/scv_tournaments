<template>
  <div>
    <h3>Seleccionar torneo</h3>
    <b-list-group>
      <b-list-group-item v-for="t in tournaments" :key="t.id" v-on:click="selectTournament(t.id)" button>{{ t.name }}
      </b-list-group-item>
    </b-list-group>
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