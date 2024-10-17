<template>
  <div class="container">
    <div class="video-section">
      <VideoPlayer />
    </div>
    <div class="interaction-section">
      <div class="input-area">
        <input v-model="userInput" placeholder="输入您的消息" />
        <button @click="sendMessage">发送</button>
      </div>
      <div class="response-area">
        <h3>回复：</h3>
        <p>{{ response }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import VideoPlayer from './VideoPlayer.vue'

const userInput = ref('')
const response = ref('')

const sendMessage = () => {
  // 这里可以添加发送消息的逻辑
  response.value = `您输入的消息是: ${userInput.value}`
  userInput.value = ''
}
</script>

<style scoped>
.container {
  display: flex;
  height: 100vh;
}

.video-section {
  flex: 1;
  padding: 20px;
}

.interaction-section {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.input-area {
  margin-bottom: 20px;
}

.input-area input {
  width: 70%;
  padding: 10px;
}

.input-area button {
  padding: 10px 20px;
  margin-left: 10px;
}

.response-area {
  flex-grow: 1;
  overflow-y: auto;
}
</style>