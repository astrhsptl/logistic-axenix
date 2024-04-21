import { WareHouse } from '@/shared';
import { SalePoint } from '@/shared/interfaces/sale-point';

interface Point {
  point: SalePoint | WareHouse;
  position: number;
  hidden: boolean;
}

export const calculate = async (items: Point[]) => {};
