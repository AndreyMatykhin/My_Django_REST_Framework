import React from 'react'

class TODOForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {title:'', project_name: '', users_list: []}
        }
    handleChange(event){
        {event.target.name=='users_list'?
            this.setState({users_list: [...event.target.options].filter(({selected}) => selected).map(({value}) => value)})
            : this.setState({[event.target.name]: event.target.value})};
    }

    handleSubmit(event) {
        this.props.createTODO(this.state.title, this.state.project_name, this.state.users_list)
        event.preventDefault()
    }
    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="Task title">Task title</label>
                        <input type="text" className="form-control" name="title" value={this.state.title}
                         onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="Project list">Project list</label>
                        <select name="project_name" className="form-control" size={this.props.projects.length>3?'3':this.props.projects.length} onChange={(event)=>this.handleChange(event)} >
                            {this.props.projects.map((project)=><option value={project.url}>{project.project_name}</option>)}
                        </select>
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
export default TODOForm