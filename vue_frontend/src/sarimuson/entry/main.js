import Vue from "vue/dist/vue.js";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '../assets/css/tailwind.css';
const Home = () => import( /* webpackChunkName: "chunk-home" */ "../components/Home.vue");

Vue.use(ElementUI)
Vue.config.productionTip = false
// Mount top level components
new Vue({
  el: "#app",
  components: {Home}
});
