<template>
  <div>
    <b-table small striped hover :items="positions"
             :fields="[{key:'name', label:'Equipo'},
                    {key:'played', label:'PJ'},
                    {key:'won', label:'PG'},
                    {key:'lost', label:'PP'},
                    {key:'tie', label:'PE'},
                    {key:'favor_goals', label:'GF'},
                    {key:'against_goals', label:'GC'},
                    {key:'goals_difference', label:'DG'},
                    {key:'score', label:'Pts'}]"
             no-border-collapse>
    </b-table>
  </div>
</template>
<script>
export default {
  props: ['positions']
}
</script>