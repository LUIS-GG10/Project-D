import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatDividerModule} from '@angular/material/divider';
import {MatListModule} from '@angular/material/list';
import {MatTableModule} from '@angular/material/table';
import {MatIconModule} from '@angular/material/icon';
import { CommonModule } from '@angular/common';
import {MatDialog} from '@angular/material/dialog';
import { ModificarComponent} from '../modificar/modificar.component';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule, MatIconButton } from '@angular/material/button';


export interface PeriodicElement {
  Type: string;
  name: string;
  Hostname: string;
  OS: string;
  IP: string;
  Physical_Server:string;
  Log_Location: string;
  Password: string;
}

const ELEMENT_DATA: PeriodicElement[] = [
  {Type:'Dev', name: 'FAS Server',Hostname:'APPSRVFSDV01', OS:'RHEL',IP: '185.162.34.102', Physical_Server: 'No', Log_Location:'/entimice/logs/fileserver.log', Password: "guanajuato"},
  {Type:'Dev', name: 'FAS Server',Hostname:'APPSRVFSDV01', OS:'RHEL',IP: '185.162.34.102', Physical_Server: 'No', Log_Location:'/entimice/logs/fileserver.log', Password: "guanajuato"},
  {Type:'Dev', name: 'FAS Server',Hostname:'APPSRVFSDV01', OS:'RHEL',IP: '185.162.34.102', Physical_Server: 'No', Log_Location:'/entimice/logs/fileserver.log', Password: "guanajuato"},
  {Type:'Dev', name: 'FAS Server',Hostname:'APPSRVFSDV01', OS:'RHEL',IP: '185.162.34.102', Physical_Server: 'No', Log_Location:'/entimice/logs/fileserver.log', Password: "guanajuato"},

  
];
@Component({
  selector: 'app-administrador',
  standalone: true,
  imports: [MatCardModule,MatDividerModule,MatListModule,MatTableModule,MatIconModule,CommonModule, MatMenuModule,MatButtonModule, MatIconButton],
  templateUrl: './administrador.component.html',
  styleUrl: './administrador.component.css'
})
export class AdministradorComponent {
  constructor(public dialog: MatDialog){}
  displayedColumns: string[] = ['Type', 'name', 'Hostname', 'OS', 'IP', 'Physical_Server', 'Log_Location', 'Password', 'symbol'];
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

