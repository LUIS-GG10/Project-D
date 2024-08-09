import {ChangeDetectionStrategy, Component, signal } from '@angular/core';
import {MatCard, MatCardActions, MatCardContent, MatCardHeader, MatCardTitle} from "@angular/material/card";
import {MatButton} from "@angular/material/button";
import {takeUntilDestroyed} from '@angular/core/rxjs-interop';
import  {MatDivider} from "@angular/material/divider";
import { MatFormField } from "@angular/material/form-field";
import { MatLabel } from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {FormControl, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import { merge } from 'rxjs';
import { HttpClient} from '@angular/common/http';
import {MatIconModule} from '@angular/material/icon';
import { Router } from '@angular/router';
import { AuthService } from '../../../auth.service';
 
@Component({
  selector: 'app-formulario',
  standalone: true,
  imports: [MatCardContent, MatCardTitle, MatCard, MatCardActions, MatCardHeader, MatButton, MatDivider,MatFormField, MatLabel, MatInputModule, FormsModule, ReactiveFormsModule, MatIconModule],
  templateUrl: './formulario.component.html',
  styleUrl: './formulario.component.css'
})

export class FormularioComponent {
onAccion() {
this.entrar = true;
this.updateErrorMessage();
if (this.PRID.valid && this.Password.valid) {
  this.sendData();
}
}
get_isSuccess(response: any){
  const fakeToken = '12345';  // Esto es solo un ejemplo
    if (this.authService.login(this.isSuccess)) {
      this.authService.setToken(fakeToken);  // Guarda el token (esto es solo un ejemplo)
      this.router.navigate(['/Principal'],{ state: { user: response }});  // Redirige a la página protegida
    } else {
      alert('Invalid credentials');
    }
}
  isSuccess=false; 
  entrar = false;
  readonly PRID = new FormControl('', [Validators.required]);
  readonly Password = new FormControl('', [Validators.required]);

  errorMessage = signal('');
  
  constructor(private router: Router, private http: HttpClient, private authService: AuthService) {
    
  }

  updateErrorMessage() {
    if(this.entrar==true){
    if (this.Password.hasError('required') || this.PRID.hasError('required')) {
      this.errorMessage.set('Password y PRID is a required field');
    }  else {
      this.errorMessage.set('');
    }
    }
  }
 
  clearErrors() {
    this.entrar = false;
    this.updateErrorMessage();
    this.errorMessage.set('');
  }
  hide = signal(true);
  clickEvent(event: MouseEvent) {
    this.hide.set(!this.hide());
    event.stopPropagation();
  }
  sendData() {
    // Encode the credentials (if necessary)
    const PRID = this.PRID.value;
    const Password = this.Password.value;
    const data={
      prid:PRID,
      password:Password
    }

  
    // Construct the request URL with the parameters
    const url = `http://127.0.0.1:5000/api/Users/Validate`;
  
    // Make the GET request
    this.http.post(url,data).subscribe(response => {
      console.log('Success:', response);
      
      this.responseValidate(response);
    }, error => {
      console.error('Error:', error);
    });
  }
  responseValidate(responsedata: any){
    if(responsedata){
      this.isSuccess = true;
      console.log(this.isSuccess);
      this.get_isSuccess(responsedata);
    }
    else{
    

    }

  }
}
