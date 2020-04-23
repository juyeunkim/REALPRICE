<template>
  <div id="small">
      <div>
      수타SUTA
      </div>
      <div class="price-font">
      19963
      </div>
  </div>
</template>

<script>
  export default {
   
  }
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');
@font-face { font-family: 'TmonMonsori'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff') format('woff'); font-weight: normal; font-style: normal; }

  .price-font {
      font-family: 'TmonMonsori';
  }


  #small{
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    
    width: 100px;
    height: 50px;
    border: solid 1px red;
    text-align: center;
  }
</style>