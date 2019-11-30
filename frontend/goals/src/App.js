import React, { Component } from 'react';
import './App.css';
import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'

import CustomLayout from './containers/Layout';
import GoalList from './containers/GoalListView';

class App extends Component {
  render () {
    return (
      <div className="App">
        <CustomLayout>
          <GoalList />
        </CustomLayout>
      </div>
    );
  }
}

export default App;
