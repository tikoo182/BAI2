import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  
  // Uvicorn URL
  readonly APIUrl = "http://127.0.0.1:8000";

  constructor(private http:HttpClient) { }

  Query(question:any):Observable<any>{
    let params1 = new HttpParams().set('question', question)
    return this.http.get<any>(this.APIUrl + '/query/', {params: params1});
  }

}
