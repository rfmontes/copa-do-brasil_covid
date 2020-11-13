# frontend


npm install bootstrap-vue axios vue-router

Importar BootstrapVue no main.js
    - import BootstrapVue from 'bootstrap-vue';
    - import 'bootstrap/dist/css/bootstrap.css'
    - import 'bootstrap-vue/dist/bootstrap-vue.css'
    - Vue.use(BootstrapVue);

Criar NavBar.vue
    - Pegar um navbar do bootstrap-vue e criar um slot

Criar Home.vue
    - Utilizar o slot do componente NavBar.vue

Criar router.js
    - Criar rota para Home.vue

Criar pasta views

Criar views para os dashboards

Adicionar views criadas no router.js

Adicionar link para redirecionar para as views no NavBar.vue

Fazer um get no site https://api.covidtracking.com/v1/us/daily.json
    - pegar dados da covid positivos para cria um grafico

importar chartsjs
    - npm install vue-chartjs chart.js --save

criar pasta charts

criar views Covid.vue e CovidContainer.vue

Rendenizar grafico Covid no Dashboard1.vue


    Após criação do Backend

criar componente Card.vue
    - pegar dados da API http://127.0.0.1:8000/v1/enquetes/times/
    - criar um botão votar

Na view Home.vue rendenizar o componente Card.vue para votar na enquete

Criar grafico com voto computados na Home
    - na pasta charts criar Time.vue e TimeContainer.vue





