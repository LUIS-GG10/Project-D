import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Pagina2Component } from './pagina2.component';

describe('Pagina2Component', () => {
  let component: Pagina2Component;
  let fixture: ComponentFixture<Pagina2Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Pagina2Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(Pagina2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
