import { createApp } from "vue";
const HelloWorld = () => import( /* webpackChunkName: "chunk-hello-world" */ "../components/HelloWorld.vue");

// Mount top level components
const app = createApp({
  components: {HelloWorld},
})
app.mount('#app')
