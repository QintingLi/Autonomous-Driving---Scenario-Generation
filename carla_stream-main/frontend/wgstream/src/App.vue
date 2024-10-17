<script setup lang="ts">
import { ref } from 'vue'
import VideoPlayer from './components/VideoPlayer.vue'

const userInput = ref('')
const response = ref('')
const videoUrl = ref('http://localhost:8000/webcam')

const sendMessage = () => {
  response.value = `您输入的消息是: ${userInput.value}`
  userInput.value = ''
}
</script>

<template>
  <div class="app">
    <header>
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="80" height="80" />
      <h1>Vue Video Player</h1>
    </header>
    <main>
      <div class="content">
        <div class="video-section">
          <VideoPlayer :videoUrl="videoUrl" />
        </div>
        <div class="interaction-section">
          <div class="input-area">
            <input v-model="userInput" placeholder="Input your information" />
            <button @click="sendMessage">发送</button>
          </div>
          <div class="response-area">
            <h3>回复：</h3>
            <p>{{ response }}</p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  box-sizing: border-box;
}

header {
  text-align: center;
  margin-bottom: 20px;
}

.logo {
  display: inline-block;
  vertical-align: middle;
  margin-right: 20px;
}

h1 {
  display: inline-block;
  vertical-align: middle;
  font-size: 24px;
  color: #42b883;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.video-section {
  width: 100%;
  aspect-ratio: 16 / 9;
  background-color: #f0f0f0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.interaction-section {
  width: 100%;
}

.input-area {
  display: flex;
  margin-bottom: 20px;
}

.input-area input {
  flex-grow: 1;
  padding: 10px;
  margin-right: 10px;
}

.input-area button {
  padding: 10px 20px;
  white-space: nowrap;
}

.response-area {
  border: 1px solid #ccc;
  padding: 10px;
  background-color: #ffffff;
  min-height: 100px;
}
</style>