import { WareHouse } from '@/shared';
import { SalePoint } from '@/shared/interfaces/sale-point';

export class PointAssociative {
  public left_point: WareHouse | SalePoint;
  public right_point: WareHouse | SalePoint;

  constructor(
    left_point: WareHouse | SalePoint,
    right_point: WareHouse | SalePoint,
  ) {
    this.left_point = left_point;
    this.right_point = right_point;
  }
}

export class Point {
  public point: WareHouse | SalePoint;
  public links: PointAssociative[] = [];

  constructor(point: WareHouse | SalePoint) {
    this.point = point;
  }
}
