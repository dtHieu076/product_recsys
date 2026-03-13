export const getOrCreateUserSession = () => {
  let session = localStorage.getItem('user_session')
  if (!session) {
    session = 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9)
    localStorage.setItem('user_session', session)
  }
  return session
}

