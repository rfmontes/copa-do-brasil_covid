<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
              <p class="titulo-pagina">Dados Covid-19 (Brasil)</p>
              <div class="card mb-4">
                  <div class="card-header titulo-grafico">
                      <i class="fas fa-chart-area mr-1"></i>
                      Casos Positivos 
                  </div>
                  <div class="card-body"><CovidBrasilContainer/></div>
              </div>
              <p class="titulo-pagina">Dados Covid-19 (EUA)</p>
              <div class="card mb-4">
                  <div class="card-header titulo-grafico">
                      <i class="fas fa-chart-area mr-1"></i>
                      Casos Positivos 
                  </div>
                  <div class="card-body"><CovidEuaContainer/></div>
              </div>
              <p class="titulo-pagina">Dados Covid-19 (Mundo)</p>
              <div class="card mb-4">
                  <div class="card-header titulo-grafico">
                      <i class="fas fa-chart-area mr-1"></i>
                      Casos Positivos 
                  </div>
                  <div class="card-body"><CovidPaisesContainer/></div>
              </div>
            </div>
        </div>
    </NavBar>
</template>

<script>
import NavBar from '../components/NavBar.vue'
import CovidEuaContainer from '../charts/CovidEuaContainer.vue'
import CovidBrasilContainer from '../charts/CovidBrasilContainer.vue'
import CovidPaisesContainer from '../charts/CovidPaisesContainer.vue'

export default {
  name: 'Dashboard1',

  components: {
    NavBar,
    CovidEuaContainer,
    CovidBrasilContainer,
    CovidPaisesContainer,
  }

}
</script>


<style scoped>

</style>