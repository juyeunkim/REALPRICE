// import axios from "./http-common";
import axios from 'axios'

const apiUrl = "http://13.125.68.33:8080/api";
// const apiUrl = "http://127.0.0.1:8000/api";
// const apiUrl = "/api";

// let header = {
//     headers: {
//         'Access-Control-Allow-Origin': '*',
//         'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
//         'Content-Type': 'application/json',
//     }
//      headers: {'Content-Type': 'application/json; charset=utf-8', "mimetype" : "applications/json"}
// }

function postRealPrice(params) {
    // console.log('Im in postQ in api/index.js');
    return axios.post(`${apiUrl}/realprice/`, params);
    // axios.post(`${apiUrl}/realprice/`, params)
    // .then(function (response) {
    //     console.log(response);
    // })
    // .catch(function (error) {
    //     console.log(error);
    // });
}

function postQna(params) {
    // console.log(params);
    // return axios.post(`${apiUrl}/qnas/`, params, header);
    return axios.post(`${apiUrl}/qnas/`, params);
}

function getStores(data) {
    return axios.post(`${apiUrl}/getStores/`, data);
}

function getFaqs() {
    return axios.get(`${apiUrl}/faqs/`);
}

function getQnas() {
    return axios.get(`${apiUrl}/qnas/`);
}

function getUsers() {
    return axios.get(`${apiUrl}/users/`);
}

function getUserInfo(params) {
    return axios.get(`${apiUrl}/users/${params}/`);
}

function deleteUser(params) {
    return axios.delete(`${apiUrl}/users/${params}/`);
}

function updateUser(params, data) {
    return axios.put(`${apiUrl}/users/${params}/`, data);
}

function signup(data) {
    return axios.post(`${apiUrl}/users/`, data)

}

function login(data) {
    return axios.post(`${apiUrl}/auth/login/`, data)
}

function checkUsedEmail(params) {
    return axios.get(`${apiUrl}/checkUsedEmail/${params}/`)
}

function detailStore(params) {
    return axios.get(`${apiUrl}/detailStore/${params}/`)
}

const Api = {
    postRealPrice,
    getStores,
    getFaqs,
    getQnas,
    postQna,

    ////// users
    signup,
    login,
    getUsers,
    getUserInfo,
    deleteUser,
    updateUser,

    // 이메일 중복체크
    checkUsedEmail,
    // 음식점 상세정보 + 리뷰
    detailStore


}


export default Api;