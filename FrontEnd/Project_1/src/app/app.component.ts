import { Component } from '@angular/core';
import { RouterOutlet,RouterModule, } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { EncabezadoComponent } from "./login/componentes/encabezado/encabezado.component";
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, LoginComponent, EncabezadoComponent,HttpClientModule,RouterModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Project_1';
}
