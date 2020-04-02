import axios from "axios";

const apiUrl = "/api";

export default {
  getStores(params) {
    return axios.get(`${apiUrl}/stores`, {
      params
    });
  },
  getFaqs() {
    return axios.get(`${apiUrl}/faqs`);
  },
  getQnas() {
    return axios.get(`${apiUrl}/qnas`);
  }
};
