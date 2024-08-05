import {useState} from 'react'
import {toast} from 'react-toastify'
import Cookies from 'js-cookie'

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const onSubmitForm = async(e) => {
        e.preventDefault()

        const userDetails = {username, password}
        const url = 'http://127.0.0.1:8000/auth/login/'
        const options = {
            method: 'POST',
            body: JSON.stringify(userDetails),
            headers: {
                'Content-Type': 'application/json',
            }
        };
        const response = await fetch(url, options)
        if(response.ok){
            const data = await response.json()
            console.log(data)
            Cookies.set('token', data.token)
            toast.success('Login Successful')
        }
        else{
            toast.error('Login Failed')
        }
    }

    return(
        <div>
            <h1>Login</h1>
            <form onSubmit={onSubmitForm}>
                <label>Username</label>
                <input
                type='text'
                value={username}
                placeholder='Enter Username'
                onChange={(e) => setUsername(e.target.value)}
                />
                <label>Password</label>
                <input
                type='password'
                value={password}
                placeholder='Enter Password'
                onChange={(e) => setPassword(e.target.value)}
                />

                <button type='submit'>Login</button>

            </form>
        </div>
    )
}

export default Login