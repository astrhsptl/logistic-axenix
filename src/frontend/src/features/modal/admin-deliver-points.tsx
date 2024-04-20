import { DefaultButton, DeliverStyle, useStoreHook } from '@/shared';
import clsx from 'clsx';
import { observer } from 'mobx-react-lite';
import React from 'react';
import toast from 'react-hot-toast';
import { BaseModal } from '.';

interface AdminDeliverPointsProps {}

export const AdminDeliverPoints: React.FC<AdminDeliverPointsProps> = observer(
  () => {
    const { pointsChooseStatement, pointsStatement } = useStoreHook();

    return (
      <BaseModal
        className={clsx(
          DeliverStyle.baseLayout,
          pointsChooseStatement.isActive ? DeliverStyle.active : '',
        )}
        statement={pointsChooseStatement}
      >
        <aside
          className={clsx(
            DeliverStyle.modalSwitcherLayout,
            pointsChooseStatement.isActive ? DeliverStyle.active : '',
          )}
          onClick={pointsChooseStatement.switchState}
        >
          <img src='/admin-side-arrow.svg' />
        </aside>
        <aside className={DeliverStyle.asideLayout}>
          <div className={DeliverStyle.title}>Маршрут</div>
          <div className={DeliverStyle.pointContainer}>
            {pointsStatement.getPoints().map(({ point, position, hidden }) => (
              <div
                key={position}
                className={clsx(
                  DeliverStyle.pointItem,
                  hidden ? '' : DeliverStyle.active,
                )}
                onClick={() => {
                  pointsStatement.switchState(position);
                }}
              >
                <img src='/admin-side-arrow.svg' /> {point.name}
                <div
                  className={clsx(
                    DeliverStyle.moreDetailed,
                    hidden ? '' : DeliverStyle.active,
                  )}
                >
                  <p>{point.address}</p>
                  <p>{point.volume} м3</p>
                  <DefaultButton
                    className={DeliverStyle.deleteButton}
                    onClick={() => {
                      pointsStatement.removePoint(position);
                    }}
                  >
                    Удалить
                  </DefaultButton>
                </div>
              </div>
            ))}
          </div>
          <DefaultButton
            className={DeliverStyle.createButton}
            onClick={() => {
              if (pointsStatement.getPoints().length < 2) {
                toast.error('Нужно выбрать хотя бы 2 объекта!');
                return;
              }
            }}
          >
            Утвердить
          </DefaultButton>
        </aside>
      </BaseModal>
    );
  },
);
