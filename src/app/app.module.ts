import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { Blank2Module } from './app-shell/blank-2/blank-2.module';
import { BlankModule } from './app-shell/blank/blank.module';
import { NavBarComponent } from './app-shell/nav-bar/nav-bar.component';
import { FooterComponent } from './app-shell/footer/footer.component';;
import { PlaylistComponent } from './playlist/playlist.component';
import { AdduserComponent } from './adduser/adduser.component'

@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    FooterComponent,
    PlaylistComponent
,
    AdduserComponent  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    Blank2Module,
    BlankModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
