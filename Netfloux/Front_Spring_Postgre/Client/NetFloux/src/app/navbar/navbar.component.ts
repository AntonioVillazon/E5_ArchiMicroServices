import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Movie } from './../movie';
import { MovieService } from './../movie.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  public movies: Movie[] = [];
  public movieName: any;

  constructor(private movieService: MovieService) {}

  ngOnInit() {
    this.getMovies();
  }

  Search() {
    if (this.movieName == "") {
      this.ngOnInit();
    } 
    else {
      this.movies = this.movies.filter(res => {
        return res.movie_name.toLocaleLowerCase().match(this.movieName.toLocaleLowerCase());
      });
    }
  }

  public getMovies(): void {
    this.movieService.getMovies().subscribe(
      (response: Movie[]) => {
        this.movies = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  public watch(movie:Movie): void {
    const container = document.getElementById('main-container');
    const iframeContainer = document.getElementById('iframeContainer');
    const button = document.createElement('button');
    button.type = 'button';
    button.style.display = 'none';
    button.setAttribute('data-toggle', 'modal');
    button.setAttribute('data-target', '#watchModal');
    if (iframeContainer)
      iframeContainer.innerHTML = '<iframe id="iframeId" class="embed-responsive-item" src="https://www.youtube.com/embed/vlDzYIIOYmM" allowfullscreen></iframe>'
    container?.appendChild(button);
    button.click();
  }

  public onOpenModal(movie: Movie): void {
    const container = document.getElementById('main-container');
    const titleId = document.getElementById("titleId");
    const bodyId = document.getElementById("bodyId");
    const button = document.createElement('button');
    button.type = 'button';
    button.style.display = 'none';
    button.setAttribute('data-toggle', 'modal');
    button.setAttribute('data-target', '#informationModal');
    if (titleId)
      titleId.innerHTML = "<h1>More information about " + movie.movie_name + "<h1>"; 
    if (bodyId)
      bodyId.innerHTML = movie.movie_synopsis;
    container?.appendChild(button);
    button.click();
  }

}
