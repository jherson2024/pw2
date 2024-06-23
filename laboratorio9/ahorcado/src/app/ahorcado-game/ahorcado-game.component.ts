import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-ahorcado-game',
  standalone: true,
  imports: [CommonModule,FormsModule,RouterLink],
  templateUrl: './ahorcado-game.component.html',
  styleUrl: './ahorcado-game.component.css'
})
export class AhorcadoGameComponent {
  palabraSecreta: string = 'ANGULAR';
  palabraOculta: string[] = [];
  intentos: number = 6;
  letrasIncorrectas: string[] = [];
  letraIngresada: string = '';
  juegoTerminado: boolean = false;
  mensajeResultado: string = '';
  imagenAhorcado: string = 'https://github.com/jherson2024/images/blob/main/ahorcado0.png?raw=true';

  constructor() {
    this.iniciarJuego();
  }

  iniciarJuego() {
    this.palabraOculta = Array(this.palabraSecreta.length).fill('_');
    this.intentos = 6;
    this.letrasIncorrectas = [];
    this.juegoTerminado = false;
    this.mensajeResultado = '';
    this.actualizarImagenAhorcado();
  }

  adivinarLetra() {
    if (this.letraIngresada.length === 0 || this.juegoTerminado) return;

    const letra = this.letraIngresada.toUpperCase();
    this.letraIngresada = '';

    if (this.palabraSecreta.includes(letra)) {
      for (let i = 0; i < this.palabraSecreta.length; i++) {
        if (this.palabraSecreta[i] === letra) {
          this.palabraOculta[i] = letra;
        }
      }
      this.verificarVictoria();
    } else {
      if (!this.letrasIncorrectas.includes(letra)) {
        this.letrasIncorrectas.push(letra);
        this.intentos--;
        this.actualizarImagenAhorcado();
      }
      this.verificarDerrota();
    }
  }

  verificarVictoria() {
    if (!this.palabraOculta.includes('_')) {
      this.juegoTerminado = true;
      this.mensajeResultado = '¡Ganaste!';
    }
  }

  verificarDerrota() {
    if (this.intentos <= 0) {
      this.juegoTerminado = true;
      this.mensajeResultado = `Perdiste! La palabra era: ${this.palabraSecreta}`;
      this.palabraOculta = this.palabraSecreta.split('');
      this.actualizarImagenAhorcado();
    }
  }

  actualizarImagenAhorcado() {
    this.imagenAhorcado = `https://github.com/jherson2024/images/blob/main/ahorcado${6 - this.intentos}.png?raw=true`;
  }
}

