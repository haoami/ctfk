// Pathify
import { make } from 'vuex-pathify'

// Data
const state = {
  drawer: null,
  drawerImage: true,
  mini: false,
  items: [
    {
      title: 'About',
      icon: 'mdi-arch',
      to: '/about',
    },
    // {
    //   title: 'User',
    //   icon: 'mdi-account',
    //   to: '/profile',
    // },
    // {
    //   title: 'Dashboard',
    //   icon: 'mdi-view-dashboard',
    //   to: '/',
    // },
    // {
    //   title: 'Regular Tables',
    //   icon: 'mdi-clipboard-outline',
    //   to: '/tables/regular/',
    // },
    // {
    //   title: 'Challenge',
    //   icon: 'mdi-format-font',
    //   to: '/challenge',
    // },
    // {
    //   title: 'Icons',
    //   icon: 'mdi-chart-bubble',
    //   to: '/components/icons/',
    // },
    {
      title: 'Usermanage',
      icon: 'mdi-format-font',
      to: '/Usermanage',
    },
    {
      title: 'Notifications',
      icon: 'mdi-bell',
      to: '/components/notifications/',
    },
    {
      title: 'add_challenge',
      icon: 'mdi-apple-safari',
      to: '/add_challenge',
    },
    {
      title: 'Teammanage',
      icon: 'mdi-animation',
      to: '/Team'
    }
  ],
}

const mutations = make.mutations(state)

const actions = {
  ...make.actions(state),
  init: async ({ dispatch }) => {
    //
  },
}

const getters = {}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
}
