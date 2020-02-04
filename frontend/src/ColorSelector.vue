<template lang="html">
  <div class="">
    <button
      type="button"
      class="button"
      :class="colors[value] === c ? 'selected' : ''"
      :style="{ backgroundColor: c }"
      @click="$emit('input', colors.indexOf(c))"
      v-for="(c, index) in colors"
      :key="index"
    >
    {{ colors[value] === c ? '&#10004;':'' }}
    </button>
  </div>
</template>

<script>
export default {
  props: ['value'],
  data: _ => ({
    colors: ['#ffffff', '#ff0000', '#ffa500', '#008000', '#0000ff', '#000000']
  })

}
</script>

<style lang="css" scoped>
.button {
  color: white;
  width: 40%;
  border: 2px lightgrey solid;
  border-radius: 5px;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
.selected {
  border: 2px black solid;
}

</style>
