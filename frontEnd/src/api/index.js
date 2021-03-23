import http from "@/utils/http";

// // 发送登录验证码
// export const sendLoginCode = (params) => http.get('/login/code', params);
// // 发送修改手机号验证码
// export const sendModifyPasswordCode = (params) => http.get('/login/modifyPasswordCode', params);
// // 验证码登录
// export const loginByCode = (params) => http.post('/login/code', params);
// 密码登录
export const loginByPwd = (params) => http.post('/users/login/', params);
// // 密码修改
// export const modifyPassword= (params) => http.put('/login/modifyPassword', params);
//fetchBalance
export const fetchBalance = (params) => http.post('/users/fetch/',params);
export const createAccount = (params) => http.post("/account/",params);
export const queryAccount = () => http.get('/account/');
export const ocr = (params) => http.post('/users/ocr/',params);
// 



