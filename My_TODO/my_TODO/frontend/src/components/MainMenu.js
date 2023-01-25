import React from 'react'
import {Link} from 'react-router-dom'


const MainMenu = () => {
    return(
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <Link to='/'> MAIN MENU</Link>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item"> <Link to='/users'>List of Users</Link></li>
                        <li class="nav-item"> <Link to='/projects'>List of Projects</Link></li>
                        <li class="nav-item"> <Link to='/TODO'>list of ToDo</Link></li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}
export default MainMenu