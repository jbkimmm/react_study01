import { useEffect } from 'react';


const useDebounce = ({ callback, timeout, args }) => {
    useEffect(() => {
        const handler = setTimeout(callback, timeout);
        return () => clearTimeout(handler);
    }, args);  // eslint-disable-line react-hooks/exhaustive-deps
};


// Debounce 클래스형 컴포넌트 속성으로 callback, timeout, args 지정 필요
export const Debounce = ({ children, ...props }) => {
    useDebounce(props);
    return children;
};


export default useDebounce;
