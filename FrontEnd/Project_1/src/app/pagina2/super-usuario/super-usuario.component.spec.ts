import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SuperUsuarioComponent } from './super-usuario.component';

describe('SuperUsuarioComponent', () => {
  let component: SuperUsuarioComponent;
  let fixture: ComponentFixture<SuperUsuarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SuperUsuarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SuperUsuarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
