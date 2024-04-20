import { DeliverPointsStatement } from './deliver-points';
import { ModalWindowStatement } from './modal-statement';

export const RootStore = {
  burgerStatement: new ModalWindowStatement(),
  adminModalStatement: new ModalWindowStatement(),
  pointsChooseStatement: new ModalWindowStatement(),
  pointsStatement: new DeliverPointsStatement(),
};

export { ModalWindowStatement };
