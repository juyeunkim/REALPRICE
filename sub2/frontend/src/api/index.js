import axios from "axios";

const apiUrl = "/api";

export default {
    postRealPrice(params) {
        // console.log('Im in postQ in api/index.js');
        return axios.post(`${apiUrl}/realprice/`, params);
        // axios.post(`${apiUrl}/realprice/`, params)
        // .then(function (response) {
        //     console.log(response);
        // })
        // .catch(function (error) {
        //     console.log(error);
        // });
    },
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
    },
    getUserInfo(params) {
        return axios.get(`${apiUrl}/users/`, params);
    }
};