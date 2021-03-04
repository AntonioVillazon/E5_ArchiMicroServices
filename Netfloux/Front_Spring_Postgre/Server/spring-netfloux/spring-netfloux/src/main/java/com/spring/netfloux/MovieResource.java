
package com.spring.netfloux;

import java.util.List;
import java.util.Optional;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;

import com.spring.netfloux.model.Movie;
import com.spring.netfloux.service.MovieService;

@RestController
@CrossOrigin(origins="http://localhost:4200", allowedHeaders="*")
@RequestMapping("/movie")
public class MovieResource {
	private final MovieService movieService;
	
	@Autowired
	public MovieResource(MovieService movieService) {
		this.movieService = movieService;
	}
	
	@GetMapping("/all")
	public ResponseEntity<List<Movie>> getAllMovies(){
		List<Movie> movies = movieService.getAllMovies();
		return new ResponseEntity<>(movies, HttpStatus.OK);
	}
	/*
	@GetMapping("/{movie_id}")
	public ResponseEntity<Optional<Movie>> getMovie(@PathVariable("movie_id") int movie_id){
		Optional<Movie> movie = movieService.getMovie(movie_id);
		return new ResponseEntity<>(movie, HttpStatus.OK);
	}
	
	
	@PostMapping("/add")
	public ResponseEntity<Movie> addMovie(@RequestBody Movie movie){
		Movie newMovie = movieService.addMovie(movie);
		return new ResponseEntity<>(newMovie, HttpStatus.CREATED);
	}
	
	@PutMapping("/update")
	public ResponseEntity<Movie> updateMovie(@RequestBody Movie movie){
		Movie updateMovie = movieService.updateMovie(movie);
		return new ResponseEntity<>(updateMovie, HttpStatus.OK);
	}
	*/
}
