import React, { useState } from "react";
import axios from 'axios';

const { REACT_APP_API_URL } = process.env;

const Index = () =>{
    const [user, setUser] = useState("");
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);
    const [userData, setUserData] = useState({});

    const getUserColor = (e) =>{
        e.preventDefault();
        axios.post(`${REACT_APP_API_URL}/query/`,{
            user: user
        }).then((response)=>{
            setUserData({
                user: user,
                color: response.data
            });
            setError(false);
        }).catch((error)=>{
            setError(true);
        })
        setLoading(false);
    }


    return (
        <div>
            <form onSubmit={getUserColor}>
                <input
                    placeholder={"usuario"}
                    value={user}
                    onChange={(e)=>{setUser(e.target.value)}}
                />
                <button
                    type={"submit"}
                >
                    Ver color favorito
                </button>
            </form>
            {
                loading ?
                <></>
                :
                <div>
                    {
                        error === true?
                        <>El usuario no existe.</>
                        :
                        <>
                            {JSON.stringify(userData)}
                        </>
                    }
                </div>
            }
        </div>
    )
}

export default Index;