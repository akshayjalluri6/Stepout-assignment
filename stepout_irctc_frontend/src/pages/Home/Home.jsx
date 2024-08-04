import { useState, useEffect } from 'react';

const Home = () => {

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('http://127.0.0.1:8000/trains/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token 5f85f38f1e13676b47d29bb3ab5bde7be603e10d`
                }
            });

            const data = await response.json();
            console.log(data);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h1>Home</h1>
        </div>
    );
}

export default Home;
