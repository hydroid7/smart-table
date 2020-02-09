<template lang="html">
  <div>
    <button v-for="i in [1, 2, 3, 4, 5]" type="button" class="plate-button" @click="shiftVisible(i - 1)">{{i}}</button>
    <button type="button" class="plate-button off-button" @click="disableAll()">Off</button>
  </div>
</template>

<script>
export default {
  props: ['display', 'color'],
  data: _ => ({
  }),
  methods: {
    disableAll () {
      this.color = 5
      this.shiftVisible(1)
    },
    shiftVisible(numberOfPlate) {
      let displayIndex = this.display
      // let currentPlate = state[displayIndex].indexOf(true)
      fetch(`/tables/led/${displayIndex}-${numberOfPlate}-${this.color}`).then((value) => {
      })
    }
  }
}
</script>

<style lang="css" scoped>
.plate-button {
  width: 40%;
  color: black;
  border: 2px solid black;
  background-color: white;
  font-size: 16px;
  border-radius: 5px;
  padding: 15px 32px;
  margin: 4px 2px;
  cursor: pointer;
}

.plate-button.off-button {
  color: white;
  background-color: black;
}
</style>
