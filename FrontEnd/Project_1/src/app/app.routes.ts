import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { Pagina2Component } from './pagina2/pagina2.component';


export const routes: Routes = [
    { path: '', component: LoginComponent },
    { path: 'Principal', component: Pagina2Component },
  ];
