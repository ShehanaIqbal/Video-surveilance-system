import { Component, OnInit } from '@angular/core';
import { link } from 'fs';
import { Source } from 'webpack-sources';

@Component({
  selector: 'app-playlist',
  templateUrl: './playlist.component.html',
  styleUrls: ['./playlist.component.css']
})
export class PlaylistComponent implements OnInit {

  constructor() { 
  //     var video_player = document.getElementById("video_player"),
  //     links=video_player.getElementsByTagName('a');
  //     for(var i=0; i<links.length;i++){
  //       links[i].onclick=handler;
  //     }
  // function handler(e){
  //   e.preventDefault();
  //   const videotarget=this.getAttribute("href");
  //   __filename=videotarget.substr(0,videotarget.lastIndexOf('.'))||videotarget;
  //   const video=document.querySelector("video_player video");
  //   video.removeAttribute('poster');
  //   const source=document.querySelectorAll("#video_player video source");
  //   source[0].src=__filename+".mp4";
  //   source[1].src=filename+".mp4";
  //   source[2].src=filename+".mp4";
  //   video.load();
  //   video.play();
//}

  }

  ngOnInit() {
  }

}
