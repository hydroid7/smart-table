<template lang="html">
  <div>
    <button class="plate-button" @click="shiftVisible">Shift Display {{display + 1}}</button>
  </div>
</template>

<script>
export default {
  props: ['display', 'color'],
  data: _ => ({
    plate: 0
  }),
  methods: {
    shiftVisible() {
      let displayIndex = this.display
      // let currentPlate = state[displayIndex].indexOf(true)
      fetch(`/tables/led/${displayIndex}-${this.plate}-${this.color}`).then((value) => {
        this.plate = (this.plate + 1) % 5
      })
    }
  }
}
</script>

<style lang="css" scoped>
.plate-button {
  width: 80%;
  color: black;
  border: 2px solid black;
  background-color: white;
  font-size: 16px;
  border-radius: 5px;
  padding: 15px 32px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>
