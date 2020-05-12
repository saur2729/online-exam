import React from 'react';
import {BrowserRouter} from "react-router-dom";
import 'typeface-roboto';

import Login from './components/auth/Login'
import SignUp from './components/auth/Signup';


function App() {
  return (
    <div>
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    </div>
  );
}

export default App;
