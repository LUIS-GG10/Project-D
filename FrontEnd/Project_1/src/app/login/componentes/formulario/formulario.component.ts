import {ChangeDetectionStrategy, Component, signal } from '@angular/core';
import {MatCard, MatCardActions, MatCardContent, MatCardHeader, MatCardTitle} from "@angular/material/card";
import {MatButton} from "@angular/material/button";
import {takeUntilDestroyed} from '@angular/core/rxjs-interop';
import{MatDivider} from "@angular/material/divider";
import { MatFormField } from "@angular/material/form-field";
import { MatLabel } from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {FormControl, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import { merge } from 'rxjs';
import { HttpClient} from '@angular/common/http';
import {MatIconModule} from '@angular/material/icon';

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

  entrar = false;
  readonly PRID = new FormControl('', [Validators.required, Validators.pattern('^[a-zA-Z]{4}[0-9]{3}$')]);
  readonly Password = new FormControl('', [Validators.required,Validators.minLength(7), Validators.pattern(/^(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$/)]);
  errorMessagePRID = signal('');
  errorMessage = signal('');
  constructor(private http: HttpClient) { // Inject HttpClient
    merge(this.PRID.statusChanges, this.PRID.valueChanges)
      .pipe(takeUntilDestroyed())
      .subscribe(() => this.updateErrorMessage());
    merge(this.Password.statusChanges, this.Password.valueChanges)
      .pipe(takeUntilDestroyed())
      .subscribe(() => this.updateErrorMessage());
  }


  updateErrorMessage() {
    if(this.entrar==true){
    if (this.PRID.hasError('required')) {
      this.errorMessagePRID.set('Prid is a required field');
    } else if (this.PRID.hasError('pattern')) {
      this.errorMessagePRID.set('Wrong Prid or Password');
    } else {
      this.errorMessagePRID.set('');
    }
    if (this.Password.hasError('required')) {
      this.errorMessage.set('Password is a required field');
    } else if (this.Password.hasError('pattern')) {
      this.errorMessage.set('Wrong Prid or Password');
    } else {
      this.errorMessage.set('');
    }
    }
  }
  
  clearErrors() {
    this.entrar = false;
    this.updateErrorMessage();
    this.errorMessage.set('');
    this.errorMessagePRID.set('');
    
  }
  hide = signal(true);

  sendData() {
    // Encode the credentials (if necessary)
    const PRID = this.PRID.value;
    const Password = this.Password.value;
  
    // Construct the request URL with the parameters
    const url = `http://127.0.0.1:5000/api/Users/${PRID},${Password}`;
  
    // Make the GET request
    this.http.get(url).subscribe(response => {
      console.log('Success:', response);
    }, error => {
      console.error('Error:', error);
    });
  }
 
}



