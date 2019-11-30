import React from 'react';
import { Route } from 'react-router-dom';

import GoalList from './containers/GoalListView';
import GoalDetail from './containers/GoalDetailView';

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={GoalList} />
        <Route exact path='/goals/' component={GoalList} />
        <Route exact path='/goals/:goalID' component={GoalDetail} />
    </div>
)

export default BaseRouter;