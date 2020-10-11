<template>
  <div>
    <h1 class="text-2xl mb-5">Recent Purchases</h1>
    <div class="m-auto">
        <el-table
        :data="tableData"
        border
        style="width: 100%"
        height="500">
        <el-table-column
          fixed
          prop="date"
          label="Date"
          :min-width="15">
        </el-table-column>
        <el-table-column
          prop="purchase_id"
          label="Purchase ID"
          :min-width="15">
        </el-table-column>
        <el-table-column
          prop="items"
          label="Items"
          :min-width="15">
        </el-table-column>
        <el-table-column
          prop="quantity"
          label="Qty"
          :min-width="15">
        </el-table-column>
        <el-table-column
          prop="total"
          label="Total(₱)"
          :min-width="15">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>


<script>
export default {
  name: 'RecentPurchasesTable',
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
