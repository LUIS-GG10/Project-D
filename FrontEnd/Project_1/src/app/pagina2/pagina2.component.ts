import {ChangeDetectionStrategy, Component, OnInit} from '@angular/core';
import { EncabezadoComponent } from '../login/componentes/encabezado/encabezado.component';
import {MatCardModule} from '@angular/material/card';
import {MatToolbar} from "@angular/material/toolbar";
import {MatIconModule} from '@angular/material/icon';
import {MatDividerModule} from '@angular/material/divider';
import {MatButtonModule} from '@angular/material/button';
import { Router, ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../app/auth.service';
import { SuperUsuarioComponent } from './componentesDU/super-usuario/super-usuario.component';
import { UsuarioComponent } from "./componentesDU/usuario/usuario.component";
import { AdministradorComponent } from "./componentesDU/administrador/administrador.component";
@Component({
  selector: 'app-pagina2',
  standalone: true,
  imports: [EncabezadoComponent, MatCardModule, MatToolbar, MatButtonModule, MatIconModule, MatDividerModule, CommonModule, SuperUsuarioComponent, UsuarioComponent, AdministradorComponent],
  templateUrl: './pagina2.component.html',
  styleUrl: './pagina2.component.css'
})
export class Pagina2Component implements OnInit{
LogOut() {
  this.router.navigate(['']);
  this.authService.logout();

}
  user: any;
  userType:string|null=''

  constructor(private route: ActivatedRoute, private router: Router, private authService: AuthService) {}

  ngOnInit(): void {
    this.userType = 'A';
   /* // Retrieve the navigation state
    this.route.paramMap.subscribe(() => {
      this.user = history.state.user;
      console.log('User data:', this.user);
    });
    console.log(localStorage)
    this.userType=localStorage.getItem('type')
  }*/
  }
}
