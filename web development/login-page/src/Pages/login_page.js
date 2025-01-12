import './login.css';

const LoginPage = () => {
    return (
        <div className="background">
            {/* <div className="form-container">
                <form className='form'>
                    <div className="form-title">Login</div>
                    <div className="form-group">
                        <label htmlFor="username" className="form-label">Username</label>
                        <input type="email" id="username" className="form-input" />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password" className="form-label">Password</label>
                        <input type="password" id="password" className="form-input" />
                    </div>
                </form>
            </div> */}
            <form className='form'>
                <div style={{display:'flex',flexDirection:'column',gap:'20px'}}>
                <div style={{color:'grey'}}>Login</div>
                <div style={{display:'flex',flexDirection:'column',gap:'3px'}}>
                <label style={{color:'orange'}}>user</label>
                <input type='email'/>
                <label style={{color:'orange'}}>password</label>
                <input type='password'/>
                </div>
                </div>
            </form>
        </div>
    );
}

export default LoginPage;
