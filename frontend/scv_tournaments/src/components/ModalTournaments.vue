<template>
  <div>
    <b-modal id="modal-tournaments" title="BootstrapVue">
      <b-table small sticky-header striped hover :items="tournaments"
               :fields="['name']" show-empty :empty-text="'No tournaments'"
               no-border-collapse>
      </b-table>
    </b-modal>
  </div>
</template>
<script>
export default {
  data() {
    return {
      meal: ''
    }
  },
  methods: {},
  props: ['tournaments']
}
</script>