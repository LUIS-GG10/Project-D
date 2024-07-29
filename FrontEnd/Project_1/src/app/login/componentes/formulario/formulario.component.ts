import { Component, signal } from '@angular/core';
import {MatCard, MatCardActions, MatCardContent, MatCardHeader, MatCardTitle} from "@angular/material/card";
import {MatButton} from "@angular/material/button";
import{MatDivider} from "@angular/material/divider";
import { MatFormField } from "@angular/material/form-field";
import { MatLabel } from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {FormControl, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import {MatIconModule} from '@angular/material/icon';
import { Router } from '@angular/router';

@Component({
  selector: 'app-formulario',
  standalone: true,
  imports: [MatCardContent, MatCardTitle, MatCard, MatCardActions, MatCardHeader, MatButton, MatDivider,MatFormField, MatLabel, MatInputModule, FormsModule, ReactiveFormsModule, MatIconModule],
  templateUrl: './formulario.component.html',
  styleUrl: './formulario.component.css'
})
export class FormularioComponent {
  entrar = false;
  readonly PRID = new FormControl('', [Validators.required]);
  readonly Password = new FormControl('', [Validators.required]);
  errorMessage = signal('');

  onAccion() {
  this.entrar = true;
  this.updateErrorMessage();
  if(this.PRID.valid && this.Password.valid){
    this.router.navigate(['/cmbiar']); }
  }
  constructor(private router: Router) {
   
  }

  updateErrorMessage() {
    if(this.entrar==true){
     if (this.PRID.hasError('required') || this.Password.hasError('required')) {
      this.errorMessage.set('All fields are required');
    }  
    else {
      this.errorMessage.set('');
    }
  }
}
  
  clearErrors() {
    this.entrar = false;
    this.errorMessage.set(''); 
   
  }
  hide = signal(true);
  clickEvent(event: MouseEvent) {
    this.hide.set(!this.hide());
    event.stopPropagation();
  }
 
}



