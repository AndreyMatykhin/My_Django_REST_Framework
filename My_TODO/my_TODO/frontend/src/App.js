import React from 'react';
//import logo from './logo.svg';
//import './App.css';
import UserList from './components/Users.js'
import ProjectsList from './components/Projects.js'
import TODOsList from './components/TODO.js'
import TODOsProjectList from './components/TODOsProject.js'

import Footer from './components/Footer.js'
import MainMenu from './components/MainMenu.js'

import {BrowserRouter, Switch, Route} from 'react-router-dom'
import axios from 'axios'

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
            'TODOs':[]
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/authapp').then(response => {
                    this.setState({'users': response.data})
                    }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/project').then(response => {
                    this.setState({'projects': response.data})
                    }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/TODO').then(response => {
                    this.setState({'TODOs': response.data})
                    }).catch(error => console.log(error))
    }

    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                    <MainMenu />
                    <Switch>
                        <Route exact path='/users' component={()=> <UserList users={this.state.users} /> }/>
                        <Route exact path='/projects' component={()=> <ProjectsList projects={this.state.projects} /> }/>
                        <Route exact path='/TODO' component={()=> <TODOsList TODOs={this.state.TODOs} /> }/>
                        <Route path='/TODO/:project' component={()=> <TODOsProjectList TODOs={this.state.TODOs} /> }/>
                        <Route exact path='/' component={()=>(<h1>Выберите пункт Меню</h1>)}/>
                        <Route component={NotFound404} />
                    </Switch>
                <Footer />
                </BrowserRouter>
            </div>
            );
    }
}

export default App;
