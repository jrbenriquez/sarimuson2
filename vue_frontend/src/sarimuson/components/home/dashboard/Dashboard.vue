<template>
    <span>
        <el-row class="flex justify-around mt-10">
            <el-button type="success" v-on:click="goToNewPurchase" round>+ Quick Purchase</el-button>
            <el-button type="success" v-on:click="goToNewPurchase" round>+ New Purchase</el-button>
        </el-row>
        <summary-section/>
        <recent-purchases-table />
    </span>
</template>

<script>
  import SummarySection from "./SummarySection.vue";
  import RecentPurchasesTable from "./RecentPurchasesTable.vue";
  export default {
    name: "Dashboard",
    components: {SummarySection, RecentPurchasesTable},
    props: {
      purchaseAdd: String
    },
    methods: {
      goToNewPurchase: function () {
        this.$emit('open-new-purchase', true);
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
  };
</script>
