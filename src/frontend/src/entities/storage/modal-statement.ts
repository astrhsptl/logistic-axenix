import { makeAutoObservable } from 'mobx';

export class ModalWindowStatement {
  isActive: boolean = false;
  keys: string[];

  constructor() {
    makeAutoObservable(this);
    this.keys = [
      'ArrowDown',
      'ArrowUp',
      'PageUp',
      'PageDown',
      'Home',
      'End',
      'Escape',
    ];
  }

  open = () => {
    this.isActive = true;
    window.addEventListener('DOMMouseScroll', this.preventDefault);
    window.addEventListener('mousewheel', this.preventDefault);
    window.addEventListener('touchmove', this.preventDefault);
    window.addEventListener('keydown', this.preventDefaultForScrollKeys);
  };

  close = () => {
    this.isActive = false;
    window.removeEventListener('DOMMouseScroll', this.preventDefault);
    window.removeEventListener('mousewheel', this.preventDefault);
    window.removeEventListener('touchmove', this.preventDefault);
    window.removeEventListener('keydown', this.preventDefaultForScrollKeys);
  };

  switchState = () => {
    if (this.isActive === false) {
      return this.open();
    }

    return this.close();
  };

  preventDefault = (e: Event) => {
    e.preventDefault();
  };

  preventDefaultForScrollKeys = (e: KeyboardEvent) => {
    if (e.key == 'Escape') {
      return this.close();
    }
    if (this.keys.includes(e.key)) this.preventDefault(e);
  };
}
