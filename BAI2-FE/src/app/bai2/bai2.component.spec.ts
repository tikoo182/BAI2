import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Bai2Component } from './bai2.component';

describe('Bai2Component', () => {
  let component: Bai2Component;
  let fixture: ComponentFixture<Bai2Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Bai2Component]
    });
    fixture = TestBed.createComponent(Bai2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
