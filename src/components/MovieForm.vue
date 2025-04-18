<template>
    <div class = "container">
      <!-- Display success or error message -->
      <div v-if="successMessage" :class="[success ? 'alert alert-success' : 'alert alert-danger']" role="alert">
        <ul v-html="successMessage"></ul>
        <!-- {{ successMessage }} -->
      </div>
  
      <form id="movieForm" @submit.prevent="saveMovie">
        <div class="form-group mb-3">
          <label for="title" class="form-label">Movie Title</label>
          <input type="text" v-model="title" name="title" class="form-control" placeholder="Enter movie title" />
        </div>
        <div class="form-group mb-3">
          <label for="description" class="form-label">Description</label>
          <textarea v-model="description" name="description" class="form-control"></textarea>
        </div>
        <div class="form-group mb-3">
          <label for="poster" class="form-label">Poster</label>
          <input type="file" ref="poster" name="poster" class="form-control-file" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
</template>
  
<script setup>
    import { ref, onMounted } from 'vue';
    
    onMounted(() => {
        getCsrfToken();
    });
    
    const title = ref('');
    const description = ref('');
    const poster = ref(null);
    const csrf_token = ref('');
    const successMessage = ref('');
    const success = ref(false); // Boolean flag to determine success or failure
  
    const getCsrfToken = () => {
        fetch('/api/v1/csrf-token')
        .then(response => response.json())
        .then(data => {
            if (data.csrf_token) {
                csrf_token.value = data.csrf_token;
            }
            
        })
        .catch(error => {
            console.error(error);
        });
    };
  
    const saveMovie = () => {
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);
        fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
        })
    .then(response => {
      if (response.ok) 
      {
        success.value = true;
        return response.json();
      } 
      else 
      {
        success.value = false;
        return response.json(); // ensures the response is retrieved
        // throw new Error('Failed to add movie');
      }
    })
    .then(data => {
  // Set successMessage based on success or error response
//   console.log(data);
        if (success.value) {
            successMessage.value = "Movie added successfully.";
            // Clear form data if successful
            title.value = '';
            description.value = '';
            poster.value.value = ''; // Clear the poster field
        } else {
            // Handle error response
            if (data.errors) {
            // Concatenate error messages to the successMessage
            console.log(data.errors);
            successMessage.value = "";
            for(let i=0; i<data.errors.length; i++) {
                successMessage.value += `<li>${data.errors[i]}</li>` ;
            }
            } else {
            // If no specific error messages, use a generic error message
            successMessage.value = "Failed to add movie. Please try again.";
            }
        }
})

    .catch(error => {
      console.error(error);
      // Handle error
    });
  };

  
  </script>
  