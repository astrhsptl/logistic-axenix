import { ModalWindowStatement } from '@/entities/';
import { CurrentModalContext, DefaultStyle } from '@/shared';
import clsx, { ClassValue } from 'clsx';
import { observer } from 'mobx-react-lite';
import { FC, ReactNode } from 'react';

interface BaseModalProps {
  children: ReactNode;
  statement: ModalWindowStatement;
  className?: ClassValue;
}

export const BaseModal: FC<BaseModalProps> = observer(
  ({ children, statement, className }) => {
    const { isActive, switchState, open, close } = statement;

    return (
      <CurrentModalContext.Provider
        value={{
          switch: switchState,
          open,
          close,
        }}
      >
        <div
          className={clsx(
            className ? className : DefaultStyle.modalBackground,
            isActive ? DefaultStyle.active : '',
          )}
        >
          {children}
        </div>
      </CurrentModalContext.Provider>
    );
  },
);
