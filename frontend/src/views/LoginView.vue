<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-200 via-blue-100 to-white py-6 flex flex-col justify-center sm:py-12 w-full relative">
    <!-- 背景装饰元素 -->
    <div class="absolute inset-0 overflow-hidden">
      <!-- 网格背景 -->
      <div class="absolute inset-0 bg-grid opacity-30"></div>
    </div>

    <div class="relative py-3 sm:max-w-xl sm:mx-auto w-full px-4 sm:px-0">
      <!-- 卡片效果 -->
      <div class="absolute inset-0 bg-gradient-to-r from-blue-400 to-blue-600 shadow-lg transform -skew-y-6 sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl"></div>
      
      <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20 w-full sm:w-auto">
        <div class="max-w-md mx-auto">
          <!-- 头部Logo区域 -->
          <div class="divide-y divide-gray-200">
            <div class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
              <div class="text-center mb-10">
                <h1 class="text-3xl font-bold text-gray-900 mb-2">欢迎使用学堂智排</h1>
                <p class="text-gray-500">基于AI算法的大学排课系统</p>
              </div>

              <!-- 登录表单 -->
              <form class="space-y-6">
                <div>
                  <label class="block text-sm font-medium text-gray-700">用户名</label>
                  <input type="text" 
                         class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                         v-model="username"
                         placeholder="请输入用户名">
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700">密码</label>
                  <input type="password" 
                         class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                         v-model="password"
                         placeholder="请输入密码">
                </div>

                <div class="flex items-center justify-between">
                  <div class="flex items-center">
                    <input type="checkbox" 
                           class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded">
                    <label class="ml-2 block text-sm text-gray-900">记住我</label>
                  </div>
                  <div class="text-sm">
                    <a href="#" class="font-medium text-blue-600 hover:text-blue-500">忘记密码？</a>
                  </div>
                </div>

                <div>
                  <button type="submit" 
                          class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                    登录
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handleLogin() {
      // 这里处理登录逻辑
      console.log('登录信息：', this.username, this.password)
    }
  }
}
</script>

<style>
.bg-grid {
  background-size: 40px 40px;
  background-image: 
    linear-gradient(to right, rgba(59, 130, 246, 0.1) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(59, 130, 246, 0.1) 1px, transparent 1px);
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}

.float {
  animation: float 6s ease-in-out infinite;
}
</style> 