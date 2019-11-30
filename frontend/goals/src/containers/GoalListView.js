import React from 'react';
import axios from 'axios';

import Goals from '../components/Goal';

const api = 'http://45.113.233.241:5000/goals/'

class GoalList extends React.Component {
    state = {
        goals: []
    }

    // been called every time the component is mounted
    componentDidMount() {
        axios.get(api) // would cause cors-headers error
            .then(res => {
                this.setState({
                    goals: res.data
                });
            })
    }

    render () {
        return (
            <Goals data={this.state.goals}/>
        )
    }
}

export default GoalList;