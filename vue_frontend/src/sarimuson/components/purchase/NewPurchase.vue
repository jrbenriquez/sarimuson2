<!-- TODO Create Single Purchase Form-->
<template>
    <div class="md:py-10 md:mx-20">
        <el-button type="info" v-on:click="goToDashboard" round>X</el-button>
        <el-switch
          class="float-right"
          style="display: block"
          v-model="bulkMode"
          active-color="#13ce66"
          inactive-color="#ff4949"
          active-text="Bulk"
          inactive-text="Single">
        </el-switch>
        <purchase-item-form />
        <el-row class="">
                <span class="text-2xl"> Purchase List </span>
                <span class="text-2xl float-right"> Total: ₱12,345.00</span>
        </el-row>
        <purchase-item-table :tableData=tableData />
          <div class="flex justify-between my-4">
            <el-button class="text-2xl" type="info">Save for Later</el-button>
            <el-button class="text-2xl" type="success">Review and Collect</el-button>
          </div>
    </div>
</template>

<script>
  import PurchaseItemTable from "./PurchaseItemTable.vue";
  import PurchaseItemForm from "./PurchaseItemForm.vue";
  export default {
    name: 'Home',
    components: {PurchaseItemTable, PurchaseItemForm},
    props: {
    },
    methods: {
      goToDashboard() {
        this.$emit('close-new-purchase', true);
      }
    },
    data() {
      return {
        bulkMode: true,
        tableData: [{
          date: '2016-05-03',
          name: 'Tom',
          state: 'California',
          city: 'Los Angeles',
          address: 'No. 189, Grove St, Los Angeles',
          zip: 'CA 90036'
        }, {
          date: '2016-05-02',
          name: 'Tom',
          state: 'California',
          city: 'Los Angeles',
          address: 'No. 189, Grove St, Los Angeles',
          zip: 'CA 90036'
        }, {
          date: '2016-05-04',
          name: 'Tom',
          state: 'California',
          city: 'Los Angeles',
          address: 'No. 189, Grove St, Los Angeles',
          zip: 'CA 90036'
        }, {
          date: '2016-05-01',
          name: 'Tom',
          state: 'California',
          city: 'Los Angeles',
          address: 'No. 189, Grove St, Los Angeles',
          zip: 'CA 90036'
        }, {
          date: '2016-05-08',
          name: 'Tom',
          state: 'California',
          city: 'Los Angeles',
          address: 'No. 189, Grove St, Los Angeles',
          zip: 'CA 90036'
        }, {
          date: '2016-05-06',
          name: 'Tom',
          state: 'California',
          city: 'Los Angeles',
          address: 'No. 189, Grove St, Los Angeles',
          zip: 'CA 90036'
        }, {
          date: '2016-05-07',
          name: 'Tom',
          state: 'California',
          city: 'Los Angeles',
          address: 'No. 189, Grove St, Los Angeles',
          zip: 'CA 90036'
        }]
      }
    }
  }
</script>

<style>
</style>
