import React from 'react';
import {BrowserRouter} from "react-router-dom";
import 'typeface-roboto';

import Home from './components/Home'


function App() {
  return (
    <div>
      <BrowserRouter>
        <Home />
      </BrowserRouter>
    </div>
  );
}

export default App;
