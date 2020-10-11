<template>
    <el-row :gutter="20" class="mt-10">
      <el-col :span="6" class="w-full md:w-1/4">
        <div class="grid-content bg-purple">
          <top-card title="Total Revenue" value="P 123,456.00"></top-card>
        </div>
      </el-col>
      <el-col :span="6" class="w-full md:w-1/4">
        <div class="grid-content bg-purple">
          <top-card title="Total Purchases" value="P 123,456.00"></top-card>
        </div>
      </el-col>
      <el-col :span="6" class="w-full md:w-1/4">
        <div class="grid-content bg-purple">
          <top-card title="Total Items" value=32></top-card>
        </div>
      </el-col>
      <el-col :span="6" class="w-full md:w-1/4">
        <div class="grid-content bg-purple">
          <top-card title="Pending Purchases" value=3></top-card>
        </div>
      </el-col>
    </el-row>
</template>

<script>
  import TopCard from "./TopCard.vue";
  export default {
    name: 'Home',
    components: {TopCard},
    props: {
      greeting: String
    },
    data () {
      return {
        staticRoot: process.env.VUE_APP_STATIC_ROOT
      }
    }
  }
</script>

<style></style>
