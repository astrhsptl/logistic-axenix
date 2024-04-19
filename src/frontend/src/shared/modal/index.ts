import { createContext, useContext } from 'react';

export interface BaseModalContextInterface {
  switch(): void;
  open(): void;
  close(): void;
}

export const CurrentModalContext =
  createContext<BaseModalContextInterface | null>(null);

export const useCurrentModalContext = () => {
  const funcs = useContext(CurrentModalContext);

  if (funcs) {
    return funcs;
  }

  throw new Error('Undefined context');
};
