<!-- MovieListView.vue -->

<template>
    <div class="container">
        <h2>Movie List</h2>
        <div class="row">
            <div class="col-md-4  rounded" v-for="movie in movies" :key="movie.id">
                <img :src="getPosterUrl(movie.poster)" alt="Poster" />
                <div style="margin-bottom: 20px;"><h3 v-html="movie.title "></h3></div> 
                <div>{{ movie.description }}</div>
            </div>
        </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  let movies = ref([]);
  
  onMounted(async () => {
    try {
      const response = await fetch('/api/v1/movies');
      movies.value = await response.json();
    } catch (error) {
      console.error(error);
    }
  });
  
  const getPosterUrl = (filename) => {
    return `/api/v1/posters/${filename}`;
  };
</script>
  
<style scoped>
    /* Styles for MovieListView component */
    img{
        max-width: 180px;
        min-height: 250px;
        float: left;
        margin-right: 20px;
        margin-left: 0px;
        padding-left: 0px;
    }

    .rounded {
        border-radius: 0.25rem; /* Adjust the value as needed */
        /* border: 1px solid black; */
        margin-bottom: 20px;
        margin-right: 20px;
        margin-left: 10px;
        min-width: 500px;
        padding-left: 0px;
        box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
        transition: transform 1s;
    }
    .rounded:hover {
        transform: scale(1.025); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
    }

    h2{
        font-size: 45px
    }

    footer{
        float: none;
    }  
</style>
  