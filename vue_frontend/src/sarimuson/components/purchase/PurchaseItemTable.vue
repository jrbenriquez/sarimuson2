<template>
        <el-table
            :data="tableData"
            :header-cell-style="{textAlign: 'center'}"
            :cell-style="{textAlign: 'right'}"
            style="width: 100%"
            max-height="500">
            <el-table-column
              fixed
              prop="date"
              label="ID"
              min-width="15">
            </el-table-column>
            <el-table-column
              prop="name"
              label="Item"
              min-width="30">
            </el-table-column>
            <el-table-column
              prop="state"
              label="Quantity"
              min-width="10">
            </el-table-column>
            <el-table-column
              prop="city"
              label="Unit (₱)"
              min-width="20">
            </el-table-column>
            <el-table-column
              prop="address"
              label="Total (₱)"
              min-width="20">
            </el-table-column>
            <el-table-column
              fixed="right"
              label=""
              min-width="10">
              <template slot-scope="scope">
                <el-button
                  @click.native.prevent="deleteRow(scope.$index, tableData)"
                  type="text"
                  size="small">
                  Remove
                </el-button>
              </template>
            </el-table-column>
      </el-table>

</template>

<script>
  export default {
      name: "PurchaseItemTable",
      props: {
          tableData: Array
      }
  }
</script>
