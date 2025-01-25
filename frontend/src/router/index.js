import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: {
        requiresAuth: false
      }
    },
  ]
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('token') // 检查是否已登录
  
  // 如果需要认证且未登录，重定向到登录页
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'login' })
  }
  // 如果已登录且访问登录页，重定向到首页
  else if (isAuthenticated && to.name === 'login') {
    next({ name: 'home' })
  }
  else {
    next()
  }
})

export default router
