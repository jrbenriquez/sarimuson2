<!-- TODO Refactor to Dashboard Component -->
<!-- TODO Dynamically swap from Dashboard and NewPurchase Component -->
<!-- Check here https://medium.com/js-dojo/simply-switching-in-between-the-components-dynamically-vue-js-a436fe10008a -->

<template>
    <div class="md:mx-20">
        <el-row class="flex justify-around mt-10">
            <el-button type="success" v-on:click="goToNewPurchase" round>+ Quick Purchase</el-button>
            <el-button type="success" v-on:click="goToNewPurchase" round>+ New Purchase</el-button>
        </el-row>
        <summary-section/>
        <recent-purchases-table />
    </div>
</template>

<script>
  import SummarySection from "./SummarySection.vue";
  import RecentPurchasesTable from "./RecentPurchasesTable.vue";
  export default {
    name: 'Home',
    components: {SummarySection, RecentPurchasesTable},
    props: {
      purchaseAdd: String
    },
    methods: {
      goToNewPurchase: function () {
        window.location.href = this.purchaseAdd;
      },
    },
    data() {
      return {
        tableData: [{
          date: '2016-05-03',
          purchase_id: 'Tom',
          items: 'California',
          quantity: 'Los Angeles',
          total: 'No. 189, Grove St, Los Angeles',
        }, {
          date: '2016-05-03',
          purchase_id: 'Tom',
          items: 'California',
          quantity: 'Los Angeles',
          total: 'No. 189, Grove St, Los Angeles',
        }, {
          date: '2016-05-03',
          purchase_id: 'Tom',
          items: 'California',
          quantity: 'Los Angeles',
          total: 'No. 189, Grove St, Los Angeles',
        }, {
          date: '2016-05-03',
          purchase_id: 'Tom',
          items: 'California',
          quantity: 'Los Angeles',
          total: 'No. 189, Grove St, Los Angeles',
        }, {
          date: '2016-05-03',
          purchase_id: 'Tom',
          items: 'California',
          quantity: 'Los Angeles',
          total: 'No. 189, Grove St, Los Angeles',
        }, {
          date: '2016-05-03',
          purchase_id: 'Tom',
          items: 'California',
          quantity: 'Los Angeles',
          total: 'No. 189, Grove St, Los Angeles',
      }]
      }
    }
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
