<template>
  <div id="app">
    <todo-list />
    <router-view/>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'
export default {
  name: 'App'
}
</script>

<style>
</style>
