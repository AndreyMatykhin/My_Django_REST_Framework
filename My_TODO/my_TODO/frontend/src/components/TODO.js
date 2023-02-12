import React from 'react'
import {Link} from 'react-router-dom'

const TODOItem = ({TODO,deleteTODO}) => {
    return (
        <tr>
            <td>{TODO.project_name}</td>
            <td>{TODO.title}</td>
            <td>{TODO.users_list}</td>
            <td>{TODO.created}</td>
            <td>{TODO.updated}</td>
            <td>{TODO.status_complete ? 'Compleate':'No compleate'}</td>
            <td><button onClick={()=>deleteTODO(TODO.url)} type='button'>Delete</button></td>
        </tr>
    )
}
const TODOsList = ({TODOs,deleteTODO}) => {
    return (
        <div>
        <table>
            <th>Project name</th>
            <th>Title</th>
            <th>Users list</th>
            <th>Create time</th>
            <th>Update time</th>
            <th>Status complete</th>
            {TODOs.map((item) => <TODOItem TODO={item} deleteTODO={deleteTODO}/>)}
        </table>
        <Link to='/TODO/create'>Create</Link>
        </div>
    )
}
export default TODOsList