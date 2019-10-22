import React from 'react'

class ActivityItem extends React.Component {
    render() {
        const { activity } = this.props;
        return (
            <div className="content">
                <div className="line"></div>

                {/* Timeline item */}
                <div className="item">
                    <div className="avatar">
                        <img
                            alt={activity.text}
                            src={activity.user.avatar}
                        />
                        {activity.user.name}
                    </div>

                    <span className="time">
                        {activity.timestamp}
                    </span>
                    <p>{activity.text}</p>
                    <div className="commentCount">
                        {activity.comments.length}
                    </div>
                </div>

                {/* ... */}

            </div>
        )
    }
}

class Content extends React.Component {
    render() {
        const { activities } = this.props;
        return (
            <div className="content">
                <div className="line">
                    {activities.map((activity) => (
                        <ActivityItem
                            activity={activity} />
                    ))}
                </div>
            </div>
        )
    }
}

export default Content