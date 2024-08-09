import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { Pagina2Component } from './pagina2/pagina2.component';
import { AuthGuard } from './auth.guard';
import { importProvidersFrom } from '@angular/core';
import { RecuperarPasswordComponent } from './recuperar-password/recuperar-password.component';

export const routes: Routes = [
    { path: '', component: LoginComponent },
    { path: 'Principal', component: Pagina2Component ,canActivate:[AuthGuard] }, { path: 'ForgotPassword', component: RecuperarPasswordComponent},
    { path: '', redirectTo: '/login', pathMatch: 'full' }
  ];
