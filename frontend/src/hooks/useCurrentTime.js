import { useEffect, useState } from 'react';


const useCurrentTime = () => {
    const [currentTime, setCurrentTime] = useState('');

    useEffect(() => {
        const currentTime = (new Date()).toISOString().slice(11, 19);
        const handler = setInterval(() => setCurrentTime(currentTime), 1000);
        return () => clearInterval(handler);
    }, []);

    return currentTime;
};


export default useCurrentTime;
