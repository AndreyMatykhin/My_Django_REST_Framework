import React from 'react'

const TODOItem = ({TODO}) => {
    return (
        <tr>
            <td>{TODO.project_name}</td>
            <td>{TODO.users_list}</td>
            <td>{TODO.create_time}</td>
            <td>{TODO.update_time}</td>
            <td>{TODO.status_complete ? 'Compleate':'No compleate'}</td>
        </tr>
    )
}
const TODOsList = ({TODOs}) => {
    return (
        <table>
            <th>Project name</th>
            <th>Users list</th>
            <th>Create time</th>
            <th>Update time</th>
            <th>Status complete</th>
            {TODOs.results.map((item) => <TODOItem TODO={item} />)}
        </table>
    )
}
export default TODOsList