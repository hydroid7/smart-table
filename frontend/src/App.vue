<template>
  <div id="app">
    <h1>SmartTable Control</h1>
    <color-selector v-model="color"></color-selector>
    <div style="margin-top: 50px;">
      <div class="group">
        <h3>Group left</h3>
        <h5>Activity</h5>
        <plate-controller :color="color" :display="1" @shift="shiftVisible(1)"></plate-controller>
        <h5>Emotions</h5>
        <plate-controller :color="color" :display="0" @shift="shiftVisible(0)"></plate-controller>
      </div>
      <hr>
      <div class="group">
        <h3>Group right</h3>
        <h5>Emotions</h5>
        <plate-controller :color="color" :display="2" @shift="shiftVisible(2)"></plate-controller>
        <h5>Activity</h5>
        <plate-controller :color="color" :display="3" @shift="shiftVisible(3)"></plate-controller>
      </div>
    </div>
  </div>
</template>

<script>
import PlateController from './PlateController'
import ColorSelector from './ColorSelector'

export default {
  name: 'app',
  components: {
    PlateController,
    ColorSelector
  },
  data () {
    return {
      display: undefined,
      plate: undefined,
      color: 0
    }
  },
  methods: {
    shiftVisible(displayIndex) {
      let currentPlate = state[displayIndex].indexOf(true)
      this.plate = (currentPlate + 1) % 5
      fetch(`/tables/led/${displayIndex}-${this.plate}-${this.color}`).then((value) => {
        console.log(value)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}


</style>
