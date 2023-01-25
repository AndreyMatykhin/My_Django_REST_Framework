import React from 'react'
import {Link} from 'react-router-dom'

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td><Link to={`TODO/${project.project_name}`}>{project.project_name}</Link></td>
            <td>{project.users_list}</td>
            <td>{project.create_time}</td>
            <td>{project.status_complete ? 'Compleate':'No compleate'}</td>
        </tr>
    )
}
const ProjectsList = ({projects}) => {
    return (
        <table>
            <th>Project name</th>
            <th>Users list</th>
            <th>Create time</th>
            <th>Status complete</th>
            {projects.results.map((item) => <ProjectItem project={item} />)}
        </table>
    )
}
export default ProjectsList