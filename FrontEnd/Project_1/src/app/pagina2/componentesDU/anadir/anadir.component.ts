import { Component } from '@angular/core';
import {MatCard, MatCardActions, MatCardContent, MatCardHeader, MatCardTitle} from "@angular/material/card";
import  {MatDivider} from "@angular/material/divider";
import { MatFormField } from "@angular/material/form-field";
import { MatLabel } from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {MatIconModule} from '@angular/material/icon';

@Component({
  selector: 'app-anadir',
  standalone: true,
  imports: [MatCardContent, MatCardTitle, MatCard, MatCardActions, MatCardHeader, MatDivider,MatFormField, MatLabel, MatInputModule],
  templateUrl: './anadir.component.html',
  styleUrl: './anadir.component.css'
}
)

export class AnadirComponent {
onAccion() {
throw new Error('Method not implemented.');
}
}
