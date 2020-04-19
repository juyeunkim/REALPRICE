import api from "../../api";
// initial state
const state = {
    searchRealPrice: [],
    storeSearchList: [],
    storeSearchPage: "1",
    faqList: [],

    qnaList: [],
    store: {
        id: "",
        name: "",
        branch: "",
        area: "",
        tel: "",
        address: "",
        lat: 0.0,
        lng: 0.0,
        categories: []
    },

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

    // user정보
    userInfo: {
        email: "",
        first_name: "",
        last_name: "",
        profile: {
            gender: "",
            born_year: "",
            name: "", // 이름이 여기에 들어가있음
            address: "",
            phone: "",
            tag: "",
            photo: null
        }
    },
    // 전체 유저 정보
    userList: [],
    selectedUser: [],

    // RealPrice
    RealPrice: {
        taste: 0,
        distance: 0,
        price: 0
    },

    // Meeting
    meetings: [],





};

// actions
const actions = {
    // LOGIN, LOGOUT
    logout({ commit }) {
        commit('logout')
    },
    login({ commit }, payload) {
        commit('login', payload)
    },

    // 마이페이지
    userInfo({ commit }, payload) {
        api.getUserInfo(payload).then(res => {
            commit('userInfo', res.data)
        })
    },

    getUsers({ commit }) {
        api.getUsers().then(res => {
            console.log('actions')
            console.log(res.data.results)
            commit('getUsers', res.data.results)
        })
    },

    selectedUser({ commit }, payload) {
        console.log('action')
        console.log(payload)
        commit('selectedUser', payload)
    },




    async getStores({ commit }, params) {
        const append = params.append;
        const resp = await api.getStores(params);
        const stores = resp.data.results.map(d => ({
            id: d.id,
            name: d.store_name,
            branch: d.branch,
            area: d.area,
            tel: d.tel,
            address: d.address,
            lat: d.latitude,
            lng: d.longitude,
            categories: d.category_list
        }));

        if (append) {
            commit("addStoreSearchList", stores);
        } else {
            commit("setStoreSearchList", stores);
        }
        commit("setStoreSearchPage", resp.data.next);
    },

    async getFaqs({ commit }) {
        const resp = await api.getFaqs();
        const faqs = resp.data.results.map(d => ({
            no: d.faq_no,
            title: d.faq_title,
            content: d.faq_content,
            writer: d.faq_writer,
            write_date: d.faq_write_date,
            count: d.faq_count,
        }));

        commit("setFaqList", faqs);
    },
    async getQnas({ commit }) {
        const resp = await api.getQnas();
        const qnas = resp.data.results.map(d => ({
            no: d.qna_no,
            title: d.qna_title,
            question: d.qna_title,
            answer: d.qna_content,
            writer: d.qna_writer,
            write_date: d.qna_write_date,
            count: d.qna_count,
            lock: d.qna_lock > 0 ? true : false,
        }));
        commit("setQnaList", qnas);
    },
    postQuestion({ commit }, params) {
        console.log('postQuestion')
        console.log(params)
        api.postQna(params)
            .then(res => {
                console.log(res)
                    // commit("postQuestion", res.data)
            })

    },
};

// mutations
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

    // 마이페이지
    userInfo(state, payload) {
        state.userInfo = payload
    },

    // 모든 유저 불러오기
    getUsers(state, payload) {
        console.log(payload)
        state.userList = payload
    },

    selectedUser(state, payload) {
        console.log('mutation')
        console.log(payload)
        state.selectedUser = payload
    },

    setStoreSearchList(state, stores) {
        state.storeSearchList = stores.map(s => s);
    },
    addStoreSearchList(state, stores) {
        state.storeSearchList = state.storeSearchList.concat(stores);
    },
    setStoreSearchPage(state, url) {
        state.storeSearchPage = new URL(url).searchParams.get("page");
    },

    setFaqList(state, faqs) {
        state.faqList = faqs.map(s => s);
    },
    setQnaList(state, qnas) {
        state.qnaList = qnas.map(s => s);
    },

    addQnaList(state, question) {
        state.qnaList = state.qnaList.concat(question);
    },
    setRealPrice(state, list) {
        state.searchRealPrice = list;
    },
    clearRealPrice(state) {
        state.searchRealPrice = [];
    },
};

// getters
const getters = {
    userStatus: (state) => {
        return state.Session.user.pk
    },
    userInfo: (state) => {
        return state.userInfo
    },
    RealPrice: (state) => {
        return state.RealPrice
    },
    users: (state) => {
        return state.userList
    },
    selectedUser: (state) => {
        return state.selectedUser
    },
    qnaList: (state) => {
        return state.qnaList
    }
};

export default {
    namespaced: true,
    state,
    actions,
    mutations,
    getters
};