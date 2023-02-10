import React from 'react'
import {Link} from 'react-router-dom'

const ProjectItem = ({project,deleteProject}) => {
    return (
        <tr>
            <td><Link to={`TODO/${project.project_name}`}>{project.project_name}</Link></td>
            <td>{project.users_list}</td>
            <td>{project.create_time}</td>
            <td>{project.status_complete ? 'Compleate':'No compleate'}</td>
            <td><button onClick={()=>deleteProject(project.url)} type='button'>Delete</button></td>
        </tr>
    )
}
const ProjectsList = ({projects,deleteProject}) => {
    return (
        <table>
            <th>Project name</th>
            <th>Users list</th>
            <th>Create time</th>
            <th>Status complete</th>
            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
        </table>
    )
}
export default ProjectsList