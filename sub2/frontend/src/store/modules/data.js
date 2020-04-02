import api from "../../api";

// initial state
const state = {
  storeSearchList: [],
  storeSearchPage: "1",
  faqList: [
    {
      title: 'Q. 회원가입은 어떻게 하나요?',
      subtitle: "A. 우측 상단의 회원가입 버튼을 누르세요. 회원이 되시면 다양한 서비스를 누릴 수 있습니다.",
    },
    {
      title: 'Q. 로그인은 어떻게 하나요?',
      subtitle: "A. 우측 상단의 로그인 버튼을 누르세요. 로그인을 하시면 다양한 서비스를 누릴 수 있습니다. 로그인 후 필요한 검색 기능을 활용하세요. 회원이라면 누구나 이용할 수 있는 서비스입니다.",
    },
    {
      title: 'Q. 회원 탈퇴하고 싶어요.',
      subtitle: 'A. ㄹㅇ?',
    },
  ],

  qnaList: [
    {
      title: 'Q. 회원가입은 어떻게 하나요?',
      writer: '전경윤',
      question: '회원가입의 방법에 대해 무척 궁금합니다.',
      answer: "A. 우측 상단의 회원가입 버튼을 누르세요. 회원이 되시면 다양한 서비스를 누릴 수 있습니다.",
      lock: false,
    },
    {
      title: 'Q. 로그인은 어떻게 하나요?',
      writer: '백창현',
      question: '로그인 방법에 대해 무척 궁금합니다.',
      answer: "A. 우측 상단의 로그인 버튼을 누르세요. 로그인을 하시면 다양한 서비스를 누릴 수 있습니다. 로그인 후 필요한 검색 기능을 활용하세요. 회원이라면 누구나 이용할 수 있는 서비스입니다.",
      lock: false,
    },
    {
      title: 'Q. 회원 탈퇴하고 싶어요.',
      writer: '정구헌',
      question: '회원 탈퇴를 하고 싶은데 어디서 하는지 찾지 못하겠습니다.',
      answer: 'A. ㄹㅇ??',
      lock: false,
    },
    {
      title: 'Q. 코딩하기 싫어요.',
      writer: '박정환',
      question: '코딩이 싫은데 대신 해주실 분 구합니다.',
      lock: false,
    },
    {
      title: 'Q. 100만원만 주세요.',
      writer: '김주연',
      question: '백만원만 주실 분 구합니다.',
      lock: true,
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
  },
  postQuestion({ commit }, params){
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
