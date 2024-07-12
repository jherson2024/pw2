import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private httpClient:HttpClient) {
    console.log("Service working...");
   }
  getData(): Observable<any> {
    return this.httpClient.get<any>("https://jsonplaceholder.typicode.com/posts");
  }
}
