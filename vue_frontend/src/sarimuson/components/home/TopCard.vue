<template>
 <el-card shadow="hover" class="my-1 md:h-auto">
    <el-row class="text-lg md:text-2xl">
        {{ title }}
    </el-row>
    <el-row class="flex flex-none justify-end">
        <div class="text-xl md:text-lg">{{ value }}</div>
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
