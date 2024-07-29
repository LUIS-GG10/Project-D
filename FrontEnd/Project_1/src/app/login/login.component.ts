import { Component } from '@angular/core';
import { EncabezadoComponent } from "./componentes/encabezado/encabezado.component";
import { FormularioComponent } from "./componentes/formulario/formulario.component";

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ EncabezadoComponent, FormularioComponent],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

}
