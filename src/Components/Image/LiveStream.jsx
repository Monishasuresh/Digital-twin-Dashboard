import React, { useRef } from 'react';

const LiveStream = () => {
  return (
    <div>
        <button type='button'
            onClick={(e) => {
            e.preventDefault();
            if (typeof window !== 'undefined') {
                window.location.href = "http://192.168.2.100/";
            }
            }}>Live Stream
        </button>
    </div>
  );
};

export default LiveStream;