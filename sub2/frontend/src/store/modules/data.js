import api from "../../api";

// initial state
const state = {
  storeSearchList: [],
  storeSearchPage: "1",
  faq: [
    {
      title: '회원가입은 어떻게 하나요?',
      subtitle: "우측 상단의 회원가입 버튼을 누르세요. 회원이 되시면 다양한 서비스를 누릴 수 있습니다.",
    },
    {
      title: '로그인은 어떻게 하나요?',
      subtitle: "우측 상단의 로그인 버튼을 누르세요. 로그인을 하시면 다양한 서비스를 누릴 수 있습니다. 로그인 후 필요한 검색 기능을 활용하세요. 회원이라면 누구나 이용할 수 있는 서비스입니다.",
    },
    {
      title: '회원 탈퇴하고 싶어요.',
      subtitle: 'ㄹㅇ??',
    },
  ],

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
  }
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
  }
};

export default {
  namespaced: true,
  state,
  actions,
  mutations
};
