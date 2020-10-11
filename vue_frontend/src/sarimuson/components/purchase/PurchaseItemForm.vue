<template>
    <el-form class="md:py-10" ref="addItemForm" label-width="120px">
        <el-form-item class="text-2xl" label="Item name:">
            <el-input class="text-2xl" v-model="form.itemName" placeholder="Search for Item..." autofocus></el-input>
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
</template>

<script>
    export default {
        name: "PurchaseItemForm",
        data () {
            return {
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
            }
        },
        mounted() {
        },
        methods: {
        }
    }
</script>
