import { DeliverPointsStatement } from './deliver-points';
import { ModalWindowStatement } from './modal-statement';

export const RootStore = {
  burgerStatement: new ModalWindowStatement(),
  salePointStatement: new ModalWindowStatement(),
  productCreateStatement: new ModalWindowStatement(),
  adminModalStatement: new ModalWindowStatement(),
  pointsChooseStatement: new ModalWindowStatement(),
  pointsStatement: new DeliverPointsStatement(),
};

export { ModalWindowStatement };
