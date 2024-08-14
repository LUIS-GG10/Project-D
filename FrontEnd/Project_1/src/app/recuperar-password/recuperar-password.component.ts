import { Component } from '@angular/core';
import { EncabezadoComponent } from '../login/componentes/encabezado/encabezado.component';
import {MatCardModule} from "@angular/material/card";
import { MatFormField } from "@angular/material/form-field";
import { MatLabel } from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {FormsModule} from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-recuperar-password',
  standalone: true,
  imports: [EncabezadoComponent, MatCardModule, MatFormField, MatLabel, MatInputModule, MatFormFieldModule, FormsModule],
  templateUrl: './recuperar-password.component.html',
  styleUrl: './recuperar-password.component.css'
})
export class RecuperarPasswordComponent{
constructor(private router:Router) {}
onclick(){
  console.log('clicked')
  this.router.navigate(['/'])
}
}
