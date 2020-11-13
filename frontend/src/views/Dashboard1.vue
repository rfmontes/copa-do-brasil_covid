<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
              <p class="titulo-pagina">Dados Covid-19 (EUA)</p>
              <div class="card mb-4">
                  <div class="card-header titulo-grafico">
                      <i class="fas fa-chart-area mr-1"></i>
                      Casos Positivos 
                  </div>
                  <div class="card-body"><CovidContainer/></div>
              </div>
            </div>
        </div>
    </NavBar>
</template>

<script>
import NavBar from '../components/NavBar.vue'
import CovidContainer from '../charts/CovidContainer.vue'

export default {
  name: 'Dashboard1',

  components: {
    NavBar,
    CovidContainer,
  }

}
</script>


<style scoped>

</style>