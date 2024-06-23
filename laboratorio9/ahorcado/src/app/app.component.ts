import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { AhorcadoGameComponent } from './ahorcado-game/ahorcado-game.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, AhorcadoGameComponent, RouterLink],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'ahorcado';
}
