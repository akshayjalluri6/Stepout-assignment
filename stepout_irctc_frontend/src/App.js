import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Home/Home';
import Login from './pages/Login/Login';

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route exact path='/' Component={Home} />
      <Route exact path='/login' Component={Login} />
    </Routes>
    </BrowserRouter>
  );
}

export default App;
