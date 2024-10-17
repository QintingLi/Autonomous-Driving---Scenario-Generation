<template>
  <div class="video-player-container">
    <img ref="videoPlayer" class="video-stream" :src="videoUrl" @error="handleError" />
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';

export default {
  name: 'VideoPlayer',
  props: {
    videoUrl: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const videoPlayer = ref(null);
    const errorMessage = ref('');

    const handleError = (error) => {
      console.error('Error loading video stream:', error);
      errorMessage.value = '无法加载视频流。请检查服务器连接。';
    };

    watch(() => props.videoUrl, () => {
      errorMessage.value = '';
    });

    onMounted(() => {
      if (videoPlayer.value) {
        videoPlayer.value.onerror = handleError;
      }
    });

    return { videoPlayer, errorMessage, handleError };
  }
};
</script>

<style scoped>
.video-player-container {
  width: 100%;
  max-width: 640px;
  margin: 0 auto;
  position: relative;
}

.video-stream {
  width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

.error-message {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
}
</style>