import { Component } from '@angular/core';
import { EncabezadoComponent } from '../login/componentes/encabezado/encabezado.component';



@Component({
  selector: 'app-pagina2',
  standalone: true,
  imports: [EncabezadoComponent],
  templateUrl: './pagina2.component.html',
  styleUrl: './pagina2.component.css'
})
export class Pagina2Component {

}
