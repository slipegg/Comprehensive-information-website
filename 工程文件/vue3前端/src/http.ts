// 引入axios
import axios from 'axios';
import router from './router'
// 请求拦截
axios.interceptors.request.use(config => {
    alert("拦截ing");
    // 判断是否存在token，如果存在的话，则每个http header都加上token
    if (localStorage.token) {//条件这么写是因为在login.vue的页面把token存入了localStorage的wxToken中
        config.headers.Authorization = localStorage.token;
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
            alert('token过期,请重新登录!');
            //  如果token过期了;我们应该清楚token
            localStorage.removeItem('wxtoken');
            //   清楚后让它跳转到登录页面去
            router.push('/login')
        } else {
            alert(error.response.data)
        }
        return Promise.reject(error);
    }
);
export default axios;