<script setup>
import {ref} from "vue";

defineProps({
  msg: {
    type: String,
    required: true
  }
})

const input = ref([])

const accessBackend = () => {
  const data = {
    'description': input.value
  }
  fetch('http://127.0.0.1:8000/prediction/', {
    method: 'POST',
    headers: {
        "Content-Type": "application/json",
      },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

</script>

<template>
  <div class="greetings">
    <div class="parent">
      <div>
        <h1 class="green">{{ msg }}</h1>
        <div class="prediction">
          <textarea :v-model="input" @input="event => input = event.target.value"/>
          <button class="button" @click="accessBackend">Predict</button>
        </div>
      </div>
      <div class="result">
        <h1 class="green">Your movie is</h1>
        <div>Drama</div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.parent {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 1fr;
  grid-gap: 30px;
}



.prediction {
  textarea {
    margin-right: 30px;
    border-radius: 15px;
    border: none;
    height: 300px;
    width: 500px
  }

  .button {
    border-radius: 15px;
    padding: 10px;
    background-color: #00bd7e;
    border: none;
    width: 150px;
  }
}

.result {
  width: 1000px
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
