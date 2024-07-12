import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { DataService, Post } from './data.service';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,HttpClientModule,CommonModule],
  providers:[DataService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'miAplicacion';
  posts: Post[]=[];
  constructor(private dataService:DataService){
    this.dataService.getData().subscribe(data=>{
      // console.log(data);
      this.posts=data;
    });
  }
}
