import React, { ReactNode, useEffect } from 'react';
import toast from 'react-hot-toast';

interface WebsocketProviderProps {
  children: ReactNode;
}

export const WebsocketProvider: React.FC<WebsocketProviderProps> = ({
  children,
}) => {
  const connection = () => {
    const conn = new WebSocket('wss://api.labofdev.ru/notification/ws/');
    conn.addEventListener('message', (data) => {
      const message = JSON.parse(data.data);
      if (message.description) {
        toast(message.description);
      }
    });
    conn.addEventListener('error', () => {
      conn.close();
      connection();
    });
    conn.addEventListener('close', () => {
      connection();
    });
  };

  useEffect(() => {
    connection();
  }, []);

  return <>{children}</>;
};
