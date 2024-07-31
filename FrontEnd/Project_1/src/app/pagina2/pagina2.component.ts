import {ChangeDetectionStrategy, Component} from '@angular/core';
import { EncabezadoComponent } from '../login/componentes/encabezado/encabezado.component';
import {MatCardModule} from '@angular/material/card';
import {MatToolbar} from "@angular/material/toolbar";
import {MatIconModule} from '@angular/material/icon';
import {MatDividerModule} from '@angular/material/divider';
import {MatButtonModule} from '@angular/material/button';


@Component({
  selector: 'app-pagina2',
  standalone: true,
  imports: [EncabezadoComponent, MatCardModule, MatToolbar,MatButtonModule,MatIconModule,MatDividerModule],
  templateUrl: './pagina2.component.html',
  styleUrl: './pagina2.component.css'
})
export class Pagina2Component {

}
