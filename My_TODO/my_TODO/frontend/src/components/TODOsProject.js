import React from 'react'
import { useParams } from 'react-router-dom'

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
const TODOsProjectList = ({TODOs}) => {
    let { project } = useParams();
    let filtered_TODOs = TODOs.filter((TODO) => TODO.project_name === project)
    return (
        <table>
            <th>Project name</th>
            <th>Users list</th>
            <th>Create time</th>
            <th>Update time</th>
            <th>Status complete</th>
            {filtered_TODOs.map((item) => <TODOItem TODO={item} />)}
        </table>
    )
}
export default TODOsProjectList