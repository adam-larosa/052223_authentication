import { useState } from 'react'
import { Link } from 'react-router-dom'

export default function Login() {
    const [ form, setForm ] = useState( {} )
    
    const updateForm = e => {
        setForm( f => {
            return { ...f, [e.target.name]: e.target.value }
        } )
    }
    
    const handleSubmit = e => {
        e.preventDefault()
        fetch( '/login', {
            method: 'POST', 
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify( form )
        } )
            .then( r => {
                if( r.ok ){
                    r.json().then( console.log )
                } else {
                    console.error( 'OH NO ALL BAD!' )
                    console.error( 'POST /login status:', r.status )
                    r.text().then( console.warn )
                }
            } )
    }
    return (
        <>
            <Link to={-1}>
                <button>back</button>
            </Link>
            <h1>log in</h1>
            <form onSubmit={ handleSubmit }>
                <div>
                    <label>
                        username:
                        <input name="name" onChange={ updateForm }/>
                    </label>
                </div>
                <div>
                    <label>
                        password:
                        <input name="password" 
                            type="password" 
                            onChange={ updateForm }
                        />
                    </label>
                </div>
                <input type="submit"/>
            </form>
        </>
    )
}