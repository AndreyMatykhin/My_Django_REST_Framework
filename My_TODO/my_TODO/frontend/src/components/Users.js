import React from 'react'

const UserItem = ({users}) => {
    return (
        <tr>
            <td>{users.username}</td>
            <td>{users.first_name}</td>
            <td>{users.last_name}</td>
            <td>{users.email}</td>
            <td>{users.user_category}</td>
        </tr>
    )
}
const UserList = ({users}) => {
    return (
        <table>
            <th>Username</th>
            <th>First name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Category</th>
            {users.results.map((users) => <UserItem users={users} />)}
        </table>
    )
}
export default UserList