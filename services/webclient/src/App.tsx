import * as React from 'react';
import { NavigationDrawer } from 'react-md';
import './App.css';

import logo from './logo.svg';

class App extends React.Component {
  public render() {
    return (
     <NavigationDrawer
        toolbarTitle="react-md with create-react-app v2"
        drawerTitle="react-app"
      >
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <h1 className="App-title">Welcome to React</h1>
          </header>
          <p className="App-intro">
            To get started, edit <code>src/App.tsx</code> and save to reload.
          </p>
        </div>
      </NavigationDrawer>
    );
  }
}

export default App;
