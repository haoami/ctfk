<template>
  <v-container class="home"
  >
    <div class="logo">
      <img
        alt="CTFK logo"
        src="../assets/7.png"
      >
    </div>
    <h1>Welcome to CTFK Plantform</h1>
  </v-container>
</template>

<script>
  export default {
    name: 'about',
  }
</script>
<style lang="scss">
  .home{
    /*background-color: white;*/
    text-align: center;
    .logo{
      margin: 70px 0;
      img{
        max-width: 100%;
        height: 100%;
      }
    }
  }
</style>
