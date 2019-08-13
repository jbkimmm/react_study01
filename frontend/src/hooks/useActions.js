import { bindActionCreators } from 'redux';
import { useDispatch } from 'react-redux';
import { useMemo } from 'react';

const useActions = (actions, deps) => {
    const dispatch = useDispatch();
    return useMemo(() => {
        if (Array.isArray(actions)) {
            return actions.map(action => bindActionCreators(action, dispatch));
        }
        else {
            return bindActionCreators(actions, dispatch); // eslint-disable-line react-hooks/exhaustive-deps
        }
    }, deps ? [dispatch, ...deps] : [dispatch]); // eslint-disable-line react-hooks/exhaustive-deps
};

export default useActions;
