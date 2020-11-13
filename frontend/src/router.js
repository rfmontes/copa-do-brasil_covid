import Vue from 'vue';
import Router from 'vue-router';

import Home from './components/Home';
import Dashboard1 from './views/Dashboard1';
import Dashboard2 from './views/Dashboard2';
import Dashboard3 from './views/Dashboard3';


Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', name: 'home', component: Home },
    { path: '/dashboard1', name: 'dashboard1', component: Dashboard1 },
    { path: '/dashboard2', name: 'dashboard2', component: Dashboard2 },
    { path: '/dashboard3', name: 'dashboard3', component: Dashboard3 },
  ]
});