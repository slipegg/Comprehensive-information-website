import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HomeDynasic from '../views/HomeDynasic.vue'
import Personal from '../views/person.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import A from '../views/A.vue'
import testApi from '../views/testApi.vue'
import Manage from '../views/Manage.vue'
const routes: Array<RouteRecordRaw> =
  // [
  //   {
  //     path: '/personal',
  //     name: 'Personal',
  //     component: Personal
  //   },
  //   {
  //     path: '/',
  //     name: 'Login',
  //     component: Login
  //   },
  //   {
  //     path: '/register',
  //     name: 'Register',
  //     component: Register
  //   }
  // ]
  [
    {
      path: '/test',
      name: 'testApi',
      component: testApi
    },
    {
      path: '/manage',
      name: 'Manage',
      meta: {
        requireAuth: true,
      },
      component: Manage
    }, {
      path: '/dynasic',
      name: 'dynasic',
      meta: {
        requireAuth: true,
      },
      component: HomeDynasic
    },
    {
      path: '/',
      name: 'hot',
      component: HomeView
    },
    {
      path: '/A',
      name: 'A',
      component: A
    },
    {
      path: '/person',
      name: 'Person',
      meta: {
        requireAuth: true,
      },
      component: () =>
        import('../views/person.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
  ]

const router = createRouter({
  // history: createWebHistory(process.env.BASE_URL),
  history: createWebHistory("/"),
  routes
})

export default router
