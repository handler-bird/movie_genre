<script setup>
import {ref} from "vue";

defineProps({
  msg: {
    type: String,
    required: true
  }
})

const input = ref('In a post-apocalyptic world where humanity teeters on the brink of extinction, a lone scientist discovers a way to send messages back in time. Desperate to alter the course of history and prevent the cataclysm that brought about their downfall, she sends a series of cryptic messages to her past self. As she navigates the dangerous landscape of her present, she races against time to decipher the clues hidden within her own memories and unlock the key to humanity\'s salvation. But with each message sent, the fabric of time grows more fragile, and she must confront the consequences of meddling with the past. "Echoes of Eternity" is a gripping sci-fi thriller that explores the complexities of time travel, the resilience of the human spirit, and the enduring power of hope in the face of despair.')
const output = ref('')

const accessBackend = () => {
  console.log(input.value)
  if (input.value === '') {
    alert('Please give a description');
  } else {

  const data = {
    'description': input.value
  }
  fetch('http://98.67.146.185/prediction/', {
    method: 'POST',
    headers: {
        "Content-Type": "application/json",
      },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      output.value = data;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
}

</script>

<template>
  <div class="greetings">
    <div class="parent">
      <div>
        <h1 class="green">{{ msg }}</h1>
        <div class="prediction">
          <textarea :v-model="input" @input="event => input = event.target.value" :placeholder="input"/>
          <button class="button" @click="accessBackend">Predict</button>
        </div>
      </div>
      <div class="result">
        <h1 class="green">The genre given your description is ...</h1>
        <div class="output">{{output}}</div>
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
    margin-top: 15px;
    border-radius: 15px;
    padding: 10px;
    background-color: #00bd7e;
    border: none;
    width: 150px;
  }
}

.result {
  width: 100%;

  .output {
    font-size: 30px;
  }
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
