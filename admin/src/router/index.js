// Imports
import Vue from 'vue'
import Router from 'vue-router'
import register from "../views/Register";
import option from "../views/Challenge";
import { trailingSlash } from '@/util/helpers'
import {
  layout,
  route,
} from '@/util/routes'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  scrollBehavior: (to, from, savedPosition) => {
    if (to.hash) return { selector: to.hash }
    if (savedPosition) return savedPosition

    return { x: 0, y: 0 }
  },
  routes: [
    layout('Default', [
      route('Dashboard'),

      // Pages
      route('UserProfile', null, '/profile'),
      route('Register',null,'components/register'),
      // Components
      route('Notifications', null, 'components/notifications'),
      route('Icons', null, 'components/icons'),
      route('Challenge', null, '/challenge'),
      // Tables
      route('Regular Tables', null, 'tables/regular'),
      route('Add_Chanllenges',null,'/add_challenge'),
      // Maps
      route('About', null, 'about'),
      route('Team',null,'Team'),
      route('Usermanage',null,'usermanage')
    ]),
    // {
    //   name:'add_challenge',
    //   path:'/option',
    //   component:option
    // }
  ],
})

export default router
