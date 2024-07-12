import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface Post {
  userId: number;
  id: number;
  title: string;
  body: string;
}

@Injectable({
  providedIn: 'root'
})

export class DataService {

  constructor(private httpClient:HttpClient) {
    console.log("Service working...");
   }
  getData(): Observable<Post[]> {
    return this.httpClient.get<Post[]>("https://jsonplaceholder.typicode.com/posts");
  }
}
