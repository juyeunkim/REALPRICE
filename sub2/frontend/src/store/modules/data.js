import api from "../../api";

// initial state
const state = {
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

    // TODO : user정보 + token값 세션에 저장
    accessToken: sessionStorage.getItem("userToken"),
    userEmail: sessionStorage.getItem("userEmail"),
    userName: sessionStorage.getItem("userName"),
    userId: sessionStorage.getItem("userId"),


};

// actions
const actions = {
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
        const question = params;
        commit("addQnaList", question)
    }
};

// mutations
const mutations = {
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
};

export default {
    namespaced: true,
    state,
    actions,
    mutations
};