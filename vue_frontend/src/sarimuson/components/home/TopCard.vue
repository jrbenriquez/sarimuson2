<template>
 <el-card shadow="hover">
    <el-row class="text-md md:text-2xl">
        {{ title }}
    </el-row>
    <el-row class="flex flex-none justify-end">
        <div class="text-lg">{{ value }}</div>
    </el-row>
  </el-card>
</template>

<script>
  export default {
    name: 'TopCard',
    props: {
      title: String,
      value: [Number, String]
    }
  }
</script>

<style>
</style>
