<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="success">
      <b-container>
        <b-navbar-brand @click="resetTournament()" href="#">Torneos App!</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <b-nav-form>
            </b-nav-form>
            <b-button
                size="sm"
                variant="light"
                class="my-2 my-sm-0"
                type="submit"
                @click="resetTournament()"
            >Cambiar Torneo
            </b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </div>
</template>
<script>
export default {
  methods: {
    resetTournament() {
      this.$parent.resetTournament();
    }
  }
}
</script>