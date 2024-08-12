import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private authenticated = false;

  login(validate: boolean): boolean {
    if (validate) { 
      this.authenticated = true;
      return true;
    }
    return false;
  }

  setToken(token: string) {
    localStorage.setItem('authToken', token);
  }
  setRole(type:string){
    localStorage.setItem('type',type)
  }

  isAuthenticated(): boolean {
    return this.authenticated || !!localStorage.getItem('authToken');
  }

  logout() {
    this.authenticated = false;
    localStorage.removeItem('authToken');
  }
}
