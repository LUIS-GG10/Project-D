import { ComponentFixture, TestBed } from '@angular/core/testing';

import { borrarComponent } from './borrar.component';

describe('BorrarComponent', () => {
  let component: borrarComponent;
  let fixture: ComponentFixture<borrarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [borrarComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(borrarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
