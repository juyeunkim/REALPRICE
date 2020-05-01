const state = {
    // session 정보
    Session: {
        token: "",
        user: {
            pk: "",
            email: "",
            username: "",
            first_name: "",
            last_name: ""
        }
    },
}

const mutations = {
    // LOGIN, LOGOUT
    logout(state) {
        state.Session.token = null
        state.Session.user.email = null
        state.Session.user.username = null
        state.Session.user.pk = null

        sessionStorage.clear()
    },
    login(state, payload) {
        state.Session = payload

        sessionStorage.setItem("pk", payload.user.pk)
        sessionStorage.setItem("email", payload.user.email)
        sessionStorage.setItem("token", payload.token)
    },
}

const actions = {
    // LOGIN, LOGOUT
    logout({ commit }) {
        commit('logout')
    },
    login({ commit }, payload) {
        commit('login', payload)
    },
}

const getters = {
    userStatus: (state) => {
        return state.Session.user.pk
    },
}

export default {
    namespaced: true,
    state,
    actions,
    mutations,
    getters
};