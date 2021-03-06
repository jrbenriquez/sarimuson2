import Vue from "vue/dist/vue.js";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/en'
import '../assets/css/tailwind.css';
const Home = () => import( /* webpackChunkName: "chunk-home" */ "../components/home/Home.vue");

Vue.use(ElementUI, { locale })
Vue.config.productionTip = false
// Mount top level components
new Vue({
  el: "#app",
  components: {Home},
});
