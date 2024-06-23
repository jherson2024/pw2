import { ApplicationConfig} from '@angular/core';
import { provideRouter } from '@angular/router';
import { AhorcadoGameComponent } from './ahorcado-game/ahorcado-game.component';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter([
      { path: 'ahorcado_game', component: AhorcadoGameComponent },
      { path: '', redirectTo: '/ahorcado_game', pathMatch: 'full' },
    ]),
    // otros proveedores
  ],
};
