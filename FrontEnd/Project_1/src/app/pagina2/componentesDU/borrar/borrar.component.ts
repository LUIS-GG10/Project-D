import { Component } from '@angular/core';
import {MatCard, MatCardActions, MatCardContent, MatCardHeader, MatCardTitle} from "@angular/material/card";
import  {MatDivider} from "@angular/material/divider";
import { MatFormField } from "@angular/material/form-field";
import { MatLabel } from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {MatIconModule} from '@angular/material/icon';
import { HttpClient} from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-modificar',
  standalone: true,
  imports: [HttpClientModule,MatCardContent, MatCardTitle, MatCard, MatCardActions, MatCardHeader, MatDivider,MatFormField, MatLabel, MatInputModule],
  templateUrl: './borrar.component.html',
  styleUrl: './borrar.component.css'
})
export class borrarComponent {
  id:string|null=''
onAccion() {
this.sendData();


}
constructor(private http: HttpClient) {
    
}
sendData() {
  // Encode the credentials (if necessary)
  const id = 2;
  const data={
    id:id
  }


  // Construct the request URL with the parameters
  const url = `http://127.0.0.1:5000/api/Principal/`+id;

  // Make the GET request
  this.http.delete(url).subscribe(response => {
    console.log('Success:', response);
    
  }, error => {
    console.error('Error:', error);
  });
}
}
