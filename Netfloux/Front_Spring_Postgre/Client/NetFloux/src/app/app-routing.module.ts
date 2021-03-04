import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { LoginComponent } from './user/login/login.component';

const routes: Routes = [
  /*{path: "", redirectTo: "login", pathMatch:"full"},*/
  {path: "login", component: LoginComponent},
  {path: "", component: AppComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
