import React from 'react';
import UserList from './components/Users.js'
import ProjectsList from './components/Projects.js'
import TODOsList from './components/TODO.js'
import TODOsProjectList from './components/TODOsProject.js'
import LoginForm from './components/Auth.js'
import {BrowserRouter, Switch, Route, Link} from 'react-router-dom'
import axios from 'axios'
import Cookies from 'universal-cookie';

const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects':[],
            'TODOs':[],
            'token':'',
            'username':''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    load_data(){
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/authapp', {headers}).then(response => {
                    this.setState({'users': response.data.results})
                    }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/project', {headers}).then(response => {
                    this.setState({'projects': response.data.results})
                    }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/TODO', {headers}).then(response => {
                    this.setState({'TODOs': response.data.results})
                    }).catch(error => {
                        console.log(error)
                        this.setState({'TODOs': []})
                    })
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {this.set_token(response.data['token'])
                                this.setState({'username':username})})
            .catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {'Content-Type': 'application/json'}
        if (this.is_authenticated()){
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    deleteProject(url) {
        const headers = this.get_headers()
        axios.delete(url, {headers, headers})
            .then(response => {this.setState({projects: this.state.projects.filter((project)=>project.url !== url)})})
            .catch(error => console.log(error))
    }



    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav mr-auto">
                            <li class="nav-item"> <Link to='/users'>List of Users</Link></li>
                            <li class="nav-item"> <Link to='/projects'>List of Projects</Link></li>
                            <li class="nav-item"> <Link to='/TODO'>list of ToDo</Link></li>
                        </ul>
                        <p>{this.is_authenticated() ? 'Username: {name}'.replace('{name}',this.state.username)
                                                    :''}</p>
                    </div>
                    <Switch>
                        <Route exact path='/users' component={()=> <UserList users={this.state.users} /> }/>
                        <Route exact path='/projects' component={()=> <ProjectsList projects={this.state.projects} deleteProject={(id)=>this.deleteProject(id)}/> }/>
                        <Route exact path='/TODO' component={()=> <TODOsList TODOs={this.state.TODOs} /> }/>
                        <Route path='/TODO/:project' component={()=> <TODOsProjectList TODOs={this.state.TODOs} /> }/>
                        <Route exact path='/' component={()=>(<h1>Выберите пункт Меню</h1>)}/>
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) =>
                                                                        this.get_token(username, password)} />} />
                        <Route component={NotFound404} />
                    </Switch>
                    <div class="col-sm-6 col-md-3 text-center">
                        <p><strong>My TODO</strong></p>
                        <p>
                            <ul class="list-unstyled">
                                <li><Link to='/'>Домашняя</Link></li>
                                <li>{this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button>
                                                                : <Link to='/login'>Login</Link>}</li>
                            </ul>
                        </p>
                        <p><strong>Мы в социальных сетях</strong></p>
                        <p><strong>Наше приложение</strong></p>
                        <div>
                            <p><small>&copy; My TODO 2023</small></p>
                        </div>
                    </div>
                </BrowserRouter>
            </div>
            );
    }
}

export default App;
