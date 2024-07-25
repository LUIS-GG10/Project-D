import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { EncabezadoComponent } from "./componentes/encabezado/encabezado.component";
import { AppComponent } from "../app.component";
import { FormularioComponent } from "./componentes/formulario/formulario.component";


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterOutlet, EncabezadoComponent,  AppComponent, FormularioComponent],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

}
