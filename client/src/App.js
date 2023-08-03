import { Routes, Route } from 'react-router-dom'
import Root from './components/Root'
import Signup from './components/Signup'
import Login from './components/Login'
import NotFound from './components/NotFound'

function App() {
  return (
    <Routes>
      <Route index element={ <Root /> } />
      <Route path="signup" element={ <Signup /> } />
      <Route path="login" element={ <Login /> } />
      <Route path="*" element={ <NotFound /> } />
    </Routes>
  );
}

export default App;
