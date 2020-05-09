import React from 'react'
import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

import Dashboard from './Dashboard'
import Home from './Home'
import About from './About'

function AllRoutes() {
  return (
    <Router>
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/about" component={About} />
        <Route
          path="/contact"
          render={() => <h1>Contact Us</h1>} />
        <Route path="*" render={() => <h1>Error</h1>} />
      </Switch>
    </Router>
  )
}

export default AllRoutes
