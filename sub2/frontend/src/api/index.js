// import axios from "./http-common";
import axios from 'axios'

// const apiUrl = "http://13.125.68.33:8080/api";
// const apiUrl = "http://127.0.0.1:8000/api";
const apiUrl = "/api";
let header = {
    headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Content-Type': 'application/json',
    }
}

function getStores(params) {
    return axios.get(`${apiUrl}/stores`, {
        params
    });
}

function getFaqs() {
    return axios.get(`${apiUrl}/faqs`);
}

function getQnas() {
    return axios.get(`${apiUrl}/qnas`);
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
const Api = {
    getStores,
    getFaqs,
    getQnas,

    ////// users
    signup,
    login,
    getUsers,
    getUserInfo,
    deleteUser,
    updateUser
}


export default Api;