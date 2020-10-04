<!-- TODO Create BulkPurchaseForm -->
       <!-- TODO Create PurchaseItemsTable-->
<!-- TODO Create Single Purchase Form-->
<template>
    <div class="md:py-10 md:mx-20">
        <el-button type="info" round>X</el-button>
        <el-switch
          class="float-right"
          style="display: block"
          v-model="bulkMode"
          active-color="#13ce66"
          inactive-color="#ff4949"
          active-text="Bulk"
          inactive-text="Single">
        </el-switch>
        <el-form class="md:py-10" ref="addItemForm" label-width="120px">
            <el-form-item class="text-2xl" label="Item name:">
                <el-input class="text-2xl" v-model="form.itemName" placeholder="Search for Item..."></el-input>
            </el-form-item>
            <el-form-item label="Quantiy:">
                <el-input-number class="mr-4" v-model="num" @change="handleChange" :min="1" :max="10"></el-input-number>
                <el-select v-model="value" placeholder="Select">
                    <el-option
                      v-for="item in options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item size="large">
              <div class="flex justify-end">
                <el-button class="text-2xl" type="success">Add Item</el-button>
              </div>
            </el-form-item>
        </el-form>
        <el-row class="">
                <span class="text-2xl"> Purchase List </span>
                <span class="text-2xl float-right"> Total: ₱12,345.00</span>
        </el-row>

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

          <div class="flex justify-end my-4">
            <el-button class="text-2xl" type="success">Review and Collect</el-button>
          </div>
    </div>
</template>

<script>
  export default {
    name: 'Home',
    components: {},
    props: {
    },
    methods: {
    },
    data() {
      return {
        bulkMode: true,
        form: {
          itemName: '',
        },
        options: [{
          value: 'Option1',
          label: 'Option1'
        }, {
          value: 'Option2',
          label: 'Option2'
        }, {
          value: 'Option3',
          label: 'Option3'
        }, {
          value: 'Option4',
          label: 'Option4'
        }, {
          value: 'Option5',
          label: 'Option5'
        }],
        value: 'pc',
        num: 1,
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
