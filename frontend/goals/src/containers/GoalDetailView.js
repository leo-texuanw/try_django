import React from 'react';
import axios from 'axios';

import { Card } from 'antd';

var api = 'http://45.113.233.241:5000/goals/'

class GoalDetail extends React.Component {
    state = {
        goal: {}
    }

    // been called every time the component is mounted
    componentDidMount() {
        const goalID = this.props.match.params.goalID;
        console.log(api + goalID);
        axios.get(`http://45.113.233.241:5000/goals/${goalID}`) // would cause cors-headers error
            .then(res => {
                this.setState({
                    goal: res.data
                });
            })
    }

    render () {
        return (
            <Card title={this.state.goal.name} >
                <p>{this.state.goal.content}</p>
            </Card>
        )
    }
}

export default GoalDetail;