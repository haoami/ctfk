import axios from 'axios';
// import vue from 'vue';
const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API,
  timeout: 50000
})

// @Summary 用户注册
// @Produce  application/json
// @Param data body {email:"string",username:"string",nickname:"string",password:"string"}
// @Router /auth/register/ [post]
export const registerAPI = (data) => {
  return service({
    url: 'auth/register',
    method: 'post',
    data: data
  })
}
export const loginAPI = (data) => {
  return service({
    url: 'auth/login',
    method: 'post',
    data: data
  })
}
export  const GetChallengesAPI = (data) => {
  return service({
    url: 'add/challenges',
    method: 'post',
    data: data
  })
}

export const AddChallengeAPI=(data) =>{
  return service({
    url: 'add/challenge',
    method: 'post',
    data: data
  })
}

export const DelChallengeAPI=(data) =>{
  return service({
    url: 'del/challenge',
    method: 'post',
    data: data
  })
}

export const SubmitFlagAPI=( data) =>{
  return service({
    url: 'submit_flag',
    method: 'post',
    data: data
  })
}
export const registerteamAPI=(data)=>{
  return service({
    url: 'registerteam',
    method: 'post',
    data:data
  })
}
export const GetTeamAPI=(data)=>{
  return service({
    url: 'get_team_data',
    method:'post',
    data
  })
}
export const GetUserAPI=(data)=>{
  return service({
    url: 'get_user',
    method:'post',
    data
  })
}
// @Summary 用户登录
// @Produce  application/json
// @Param data body {username:"string",password:"string"}
// @Router /auth/obtainToken/ [post]
export const obtainTokenAPI = (data) => {
  return service({
    url: 'auth/obtain_token/',
    method: 'post',
    data: data
  })
}

// @Summary refreshToken
// @Produce  application/json
// @Param data body {username:"string",password:"string"}
// @Router /auth/refreshToken/ [post]
export const refreshTokenAPI = (data) => {
  return service({
    url: 'auth/refresh_token/',
    method: 'post',
    data: data
  })
}

export const logoutAPI = (data) => {
  return service({
    url: 'auth/logout/',
    method: 'get',
  })
}
export const deleteAPI = (data) => {
  return service({
    url: 'auth/delete/',
    method: 'get',
    data:data
  })
}
export const getuserAPI = (data) => {
  return service({
    url: 'get_users',
    method: 'post',
    data:data
  })
}
export const deleteuserAPI = (data) => {
  return service({
    url: 'deleteuser',
    method: 'post',
    data:data
  })
}

export const lookteamAPI = (data) => {
  return service({
    url: 'lookteam',
    method: 'post',
    data:data
  })
}
