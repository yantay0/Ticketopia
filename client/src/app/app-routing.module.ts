import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {Route, RouterModule, Routes} from "@angular/router";
import {EventsComponent} from "./component/events/events.component";
import {NotFoundComponent} from "./component/not-found/not-found.component";
import {DOMAIN} from "./config";
import { LoginComponent } from './component/login/login.component';
import { SignupComponent } from './component/signup/signup.component';
import { UserInformationComponent } from './component/user-information/user-information.component';

const routes: Routes = [
  {path: '', redirectTo: DOMAIN, pathMatch: 'full'},
  {path: DOMAIN,component: EventsComponent},
  {path: `${DOMAIN}/:category`, component: EventsComponent},
  {path: 'login', component:LoginComponent},
  {path: 'signup', component:SignupComponent},
  {path: 'user-info', component:UserInformationComponent},
  {path: '**', component: NotFoundComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
