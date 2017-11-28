class Auth {
  static authenticateUser(wechatId) {
    localStorage.setItem('user_id', wechatId)
  }

  static isUserAuthenticated() {
    return localStorage.getItem('user_id') !== null;
  }

  static deauthenticate() {
    localStorage.removeItem('user_id');
  }

  static getUserId() {
    return localStorage.getItem('user_id');
  }
}

export default Auth;
