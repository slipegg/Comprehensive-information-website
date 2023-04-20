import { createApp } from 'vue'
import App from './App.vue'
import Test from './test.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus' // 引入element-plus
import 'element-plus/theme-chalk/index.css' // 引入element-plus的样式
require('./mock')


// 为什么传这三个参数，官网有详细介绍
router.beforeEach((to, from, next) => {
  // 这里的meta就是我们刚刚在路由里面配置的meta
  if (to.meta.requireAuth) {
    // 下面这个判断是自行实现到底是否有没有登录store.getters.isLogin
    if (localStorage.token) {
      // 登录就继续
      next();
    } else {
      // 没有登录跳转到登录页面，登录成功之后再返回到之前请求的页面
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    }
  } else {
    // 不需要登录的，可以继续访问
    next()
  }
});

// 引入axios
import axios from 'axios';
// import router from './router'
// 请求拦截
axios.interceptors.request.use(config => {
  // 判断是否存在token，如果存在的话，则每个http header都加上token
  if (localStorage.token) {//条件这么写是因为在login.vue的页面把token存入了localStorage的wxToken中
    config.headers.Authorization = "Token " + localStorage.token;
    console.log(config);
    // alert(localStorage.token);
  }
  return config;//赋值完后把config返回回去

}, error => {
  // 请求错误后把我们的error返回回去
  return Promise.reject(error);
})

/**
 * 响应拦截
 * ,优式在于;在页面中每次请求的时候不需要写一遍catch
 *  */

axios.interceptors.response.use(
  response => {
    //请求成功就给它返回回去
    return response;
  },
  // 请求错误
  error => {
    //错误提醒
    // 如果token过期了的话;我们也需要给一个提醒
    const { status } = error.response;//在response中有一个status 我们用es6的方式解构出来
    if (status == 401) {
      //后台定义401为token过期
      //  如果token过期了;我们应该清楚token
      localStorage.removeItem('token');
      //   清楚后让它跳转到登录页面去
      // router.push('/login')
    } else {
      return error;
      // alert("错误！")//(error.response.data)
    }
    return Promise.reject(error);
  }
);
export default axios;
createApp(App)
  .use(store)
  .use(router)
  .use(ElementPlus, { zIndex: 3000, size: 'small' }) // 使用element-plus
  .mount('#app')


// createApp(Test)
//   .use(store)
//   .use(router)
//   .use(ElementPlus, { zIndex: 3000, size: 'small' }) // 使用element-plus
//   .mount('#test')