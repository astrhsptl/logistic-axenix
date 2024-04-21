import { WareHouse } from '@/shared';
import { SalePoint } from '@/shared/interfaces/sale-point';
import { makeAutoObservable } from 'mobx';

interface Point {
  point: SalePoint | WareHouse;
  position: number;
  hidden: boolean;
}

export class DeliverPointsStatement {
  private points: Point[] = [];
  constructor() {
    makeAutoObservable(this);
  }

  getPoints() {
    return this.points;
  }

  addPoint(point: SalePoint | WareHouse) {
    if (this.points.length === 0) {
      this.points.push({ point: point, position: 0, hidden: true });
      return 'first';
    }
    this.points.push({
      position: this.points[this.points.length - 1].position + 1,
      point: point,
      hidden: true,
    });
  }

  switchState(position: number) {
    const currentPoint = this.points.find(
      (point) => point.position === position,
    );

    if (currentPoint) {
      currentPoint.hidden = !currentPoint.hidden;
    }
  }

  invalidate() {
    this.points = [];
  }

  removePoint(position: number) {
    this.points = this.points.filter((point) => !(point.position === position));
  }
}
