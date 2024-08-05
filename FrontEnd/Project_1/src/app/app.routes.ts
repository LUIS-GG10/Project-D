import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { Pagina2Component } from './pagina2/pagina2.component';
import { AuthGuard } from './auth.guard';
import { importProvidersFrom } from '@angular/core';

export const routes: Routes = [
    { path: '', component: LoginComponent },
    { path: 'Principal', component: Pagina2Component ,canActivate:[AuthGuard] },
    { path: '', redirectTo: '/login', pathMatch: 'full' }
  ];
