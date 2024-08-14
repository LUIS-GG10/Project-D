import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatDividerModule} from '@angular/material/divider';
import {MatListModule} from '@angular/material/list';
import {MatTableModule} from '@angular/material/table';
import {MatIconModule} from '@angular/material/icon';
import { CommonModule } from '@angular/common';
import {MatDialog} from '@angular/material/dialog';
import { ModificarComponent} from '../modificar/modificar.component';
export interface PeriodicElement {
  name: string;
  position: number;
  Password: string;

}

const ELEMENT_DATA: PeriodicElement[] = [
  {position: 1, name: 'Hydrogen', Password: "guanajuato"},
  {position: 2, name: 'Helium', Password: "Teamojoji" },
  {position: 3, name: 'Lithium', Password: "huracan"},
  {position: 4, name: 'Beryllium', Password: "erixmel"},
  {position: 5, name: 'Boron', Password: "balneario"},
  
];

@Component({
  selector: 'app-super-usuario',
  standalone: true,
  imports: [MatCardModule,MatDividerModule,MatListModule,MatTableModule,MatIconModule,CommonModule],
  templateUrl: './super-usuario.component.html',
  styleUrl: './super-usuario.component.css'
})
export class SuperUsuarioComponent {
  constructor(public dialog: MatDialog){}
  displayedColumns: string[] = ['position', 'name', 'Password', 'symbol'];
  dataSource = ELEMENT_DATA;
  private _isHidden = Array(this.dataSource.length).fill(true); // Array to track password visibility
 
  hide(index: number): boolean {
    return this._isHidden[index];
  }
 
  clickEvent(index: number, event: MouseEvent) {
    this._isHidden[index] = !this._isHidden[index];
    this.dataSource = [...this.dataSource]; // Update dataSource to trigger re-rendering
    event.stopPropagation();
  }

  Modificar(){
    this.dialog.open(ModificarComponent,{
      width: '20%',
      data:{}
    })

  }
}

