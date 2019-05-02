<template>
  <div class="wrapper"> 
    <div class="top-bar">TodoList</div>
    <div class="container">
      <div class="title">오늘 할 일</div>
      <div class="list">
        <div class="todo" v-for="todo in todos" v-bind:key="todo.key">
          <input type="checkbox" class="check" v-on:click="erase">
          <p class="content">{{ todo.content }}</p>
          <p class="place" >장소: {{ todo.place }}</p>
          <p class="date" >기간: {{ todo.period}} 까지</p>
        </div>
      </div>
      <div class="input-wrapper">
        <div class="input-container">
          <input type="text" class="input-content" value="내용" v-model="content">
          <input type="text" class="input-place" value="장소" v-model="place">
          <input type="text" class="input-date" value="기간" v-model="date">
        </div>
      </div>
      <input type="button" class="add" value="추가" v-on:click="writing">
    </div>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  data() {
    return {
      todos: [],
      add: false,
      value: '',
      content: '',
      place: '',
      date: ''
    }
  },
  created: function () {
    this.$http.get('/').then((result) => {
      this.todos = result.data
      console.log(result.data)
    }).catch(function (error) {
      console.log(error)
    })
  },
  methods: {
    erase: function (id) {
      this.$http.delete('/'+id).then((result) => {
        console.log(result.data)
        this.$http.get('/').then((result) => {
          this.todos = result.data
        })
      }).catch(function (error) {
        console.log(error)
      })
    },
  writing: function () {
    console.log(1)
    this.$http.post('/', JSON.stringify({'content': this.content, 'place': this.place, 'period': this.date}), {
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(function (result) {
      console.log(result.data)
      this.$http.get('/').then((result) => {
        this.todos = result.data
      })
    })
  }
}
  }
</script>

<style>
*{
  margin: 0;
  border: 0;
}
.wrapper {
  width: 100vw;
  height: 100vh;
  background-color: #E5E5E5;
  text-align: center;
}
.top-bar {
  width: 100vw;
  height: 10vh;
  background-color: #92CF73;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 40px;
  margin: 0 auto;
}
.container {
  width: 60vw;
  height: 90vh;
  background-color: white;
  text-align: center;
  display: inline-block;
}
.title {
  font-size: 30px;
  display: flex;
  justify-content: flex-start;
  margin-left: 10%;
  margin-top: 5%;
}
.list {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.todo{
  font-size: 18px;
  width: 40vw;
  height: 3vh;
  border-bottom: 1px solid lightgray;
  margin-top: 4%;
  display: flex;
  flex-direction: row;
  padding: 3px;
  color: #3E3D3D;
}
.place {
  position: relative;
  left: 40%;
  font-size: 15px;
}
.check {
  margin-right: 2%;
  width: 23px;
  height: 23px;
}
.date {
  position: relative;
  left: 50%;
  font-size: 15px;
}
.add {
  font-size: 20px;
}
.add:hover {
  cursor: pointer;
}
.input-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 3%;
  /* justify-content: space-between; */
  /* align-content: space-between; */
}
.input-container {
  width: 40vw;
  height: 3vh;
  border-bottom: 1px solid lightgray;
  display: flex;
  align-content: space-between;
  justify-content: space-between;
}
.input-content, .input-place, .input-date {
  border: 1px solid gray;
  width: 10vw;
  height: 2vh;
}

</style>
