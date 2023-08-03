import { Link } from 'react-router-dom'

export default function Root() {
    return (
        <>
            <h1>welcome!</h1>
            <div>
                <Link to="/signup"><button>sign up</button></Link>
                <Link to="/login"><button>log in</button></Link>
            </div>
        </>
    )
}