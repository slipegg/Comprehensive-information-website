<template>
  <el-input
    v-model="input"
    type="password"
    placeholder="Please input password"
    show-password
  />
            <router-link to="/login">注册账号</router-link>
</template>


<script lang="ts" setup>
import { ref } from 'vue'
const input = ref('')
</script>
