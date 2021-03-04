import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Movie } from './movie';
import { MovieService } from './movie.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'NetFloux';
  public movies: Movie[] = [];
  public movieName: any;

  constructor(private movieService: MovieService) {}

  ngOnInit() {
    this.getMovies();
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
      titleId.innerHTML = "More information about " + movie.movie_name; 
    if (bodyId)
      bodyId.innerHTML = movie.movie_synopsis;
    container?.appendChild(button);
    button.click();
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

}
