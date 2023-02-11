import React from 'react'

class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {project_name: '', users_list: []}
        }
    handleChange(event){
        {event.target.name=='users_list'?
            this.setState({users_list: [...event.target.options].filter(({selected}) => selected).map(({value}) => value)})
            : this.setState({[event.target.name]: event.target.value})};
    }

    handleSubmit(event) {
        this.props.createProject(this.state.project_name, this.state.users_list)
        event.preventDefault()
    }
    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                <label for="Project name">Project name</label>
                    <input type="text" className="form-control" name="project_name" value={this.state.project_name}
                     onChange={(event)=>this.handleChange(event)} />
                </div>
            <div className="form-group">
                <label for="Users list">Users list</label>
                    <select name="users_list" className="form-control" size='3' multiple={true} onChange={(event)=>this.handleChange(event)} >
                     {this.props.users.map((user)=><option value={user.url}>{user.username}</option>)}
                    </select>
            </div>
            <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        )
    }
}
export default ProjectForm