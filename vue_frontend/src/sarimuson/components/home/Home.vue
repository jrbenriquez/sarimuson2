<!-- TODO Refactor to Dashboard Component -->
<!-- TODO Dynamically swap from Dashboard and NewPurchase Component -->
<!-- Check here https://medium.com/js-dojo/simply-switching-in-between-the-components-dynamically-vue-js-a436fe10008a -->
<template>
    <div class="md:mx-20">
        <component
          v-on:open-new-purchase="goTo('new-purchase')"
          v-on:close-new-purchase="goTo('dashboard')"
          :is="renderedComponent" :purchaseAdd=purchaseAdd />
    </div>
</template>

<script>
  import Dashboard from './dashboard/Dashboard.vue';
  import NewPurchase from '../purchase/NewPurchase.vue';
  export default {
    name: 'Home',
    components: {Dashboard, NewPurchase},
    props: {
      purchaseAdd: String
    },
    data() {
      return {
        currentComponent: 'dashboard'
      }
    },
    computed: {
      renderedComponent() {
        if (this.currentComponent === 'new-purchase') {
          return 'new-purchase';
        } else {
          return 'dashboard';
        }
      },
    },
    methods: {
      goTo(componentName) {
        this.currentComponent = componentName;
      }
    },
  }
</script>

<style>
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
