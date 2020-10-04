import Vue from "vue/dist/vue.js";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/en'
import '@/sarimuson/assets/css/tailwind.css';
import NewPurchase from "@/sarimuson/components/purchase/NewPurchase.vue";

Vue.use(ElementUI, { locale })
Vue.config.productionTip = false
// Mount top level components
new Vue({
  el: "#newpurchase",
  components: {NewPurchase},
});
