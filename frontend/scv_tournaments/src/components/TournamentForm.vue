<template>
  <div>
    <h4 class="mt-4">Nuevo Torneo</h4>
    <b-alert v-model="showErrors" variant="danger">{{ errors }}</b-alert>
    <b-form @submit="onSubmit">
      <b-form-group id="input-group-2" label="Nombre:" label-for="input-2">
        <b-form-input
            id="input-2"
            v-model="form.name"
            required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Cantidad de Equipos:" label-for="input-2">
        <b-form-input
            id="input-2"
            v-model="form.quantity"
            type="number"
            required
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Guardar</b-button>
    </b-form>

  </div>
</template>

<script>
const axios = require('axios');
export default {
  data() {
    return {
      form: {
        name: '',
        quantity: '',
      },
      showErrors: false,
      errors: null
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      axios.post('/backend/api/tournament/', {name: this.form.name, quantity: this.form.quantity}, {
        params: {
          format: 'json',
        }
      }).then((response) => {
        this.$parent.selectTournament(response.data.id);
      })
          .catch((error) => {
            console.log(error.response.data)
            if (error.response.data.quantity) {
              this.showErrors = true
              this.errors = error.response.data.quantity.join()
            }
          })
    },
  }
}
</script>