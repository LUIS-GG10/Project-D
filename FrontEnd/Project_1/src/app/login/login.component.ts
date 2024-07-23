import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { EncabezadoComponent } from "./componentes/encabezado/encabezado.component";
import { CuadritoComponent } from "./componentes/cuadrito/cuadrito.component";
import { AppComponent } from "../app.component";
@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterOutlet, EncabezadoComponent, CuadritoComponent, AppComponent],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

}
