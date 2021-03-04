import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { RestapiService } from 'src/app/restapi.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username: string = "";
  password: string = "";
  message: any

  constructor(private service: RestapiService, private router: Router) { }

  ngOnInit(): void {
  }

  doLogin() {
    alert(this.username + " " + this.password);
    /*let resp = this.service.login(this.username, this.password);
    resp.subscribe(data=>{
      console.log(data);
      this.router.navigate([""]);
    })*/
    if (this.username == "user" && this.password == "user"){
      this.router.navigate([""]);
    }
  }

}
