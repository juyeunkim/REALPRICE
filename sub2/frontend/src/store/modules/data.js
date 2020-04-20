import api from "../../api";
// initial state
const state = {
    realPriceList: [{
        "id": 161602,
        "store_name": "민들레",
        "branch": "",
        "area": "역삼",
        "tel": "02-566-8070",
        "address": "서울특별시 강남구 역삼동 669-16 2층",
        "latitude": 37.502589,
        "longitude": 127.037222,
        "category": "즉석떡볶이|수제튀김\r",
        "avg_score": 4.5,
        "cnt_review": 2,
        "distance": 0.143,
        "avg_price": 5400.0
    },],
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
            lock: d.qna_lock > 0 ? true : false,
        }));
        commit("setQnaList", qnas);
    },
    async postQuestion({ commit }, p) {
        console.log('postQuestion')
        // console.log(p)
        const resp = await api.postQna({
            qna_title: p.title,
            qna_writer: p.writer,
            qna_content: p.question,
            // lock: this.lock
            // 임시로 값넣어놈 ----start
            qna_write_date: p.write_date, 
            qna_group_no: p.qna_group_no,
            qna_group_order: p.qna_group_order,
            qna_depth: p.qna_depth,
        });    
        console.log(resp);
        commit("addQnaList", p)
    },
    async postRealPrice({ commit }, params) {
        console.log('postRealPrice')
        console.log(params);
        const resp = await api.postRealPrice(params);    
        console.log(resp);
        commit("setRealPrice", resp.data.received_data.result);
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
        console.log(state.qnaList);
    },
    setRealPrice(state, list) {
        state.realPriceList = list;
    },
    clearRealPrice(state) {
        state.realPriceList = [];
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