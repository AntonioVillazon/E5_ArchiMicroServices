
package com.spring.netfloux.service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.netfloux.model.Movie;
import com.spring.netfloux.repository.MovieRepository;

@Service
public class MovieService {
	
	private final MovieRepository movieRepository;
	
	@Autowired
	public MovieService(MovieRepository movieRepository) {
		this.movieRepository = movieRepository;
	}
	
	public Movie addMovie(Movie movie) {
		movie.setMovie_name(UUID.randomUUID().toString());
		return movieRepository.save(movie);
	}
	
	public Optional<Movie> getMovie(int movie_id) {
		return movieRepository.findById(movie_id);
	}
	
	public List<Movie> getAllMovies() {
		return movieRepository.findAll();
	}
	
	public Movie updateMovie(Movie movie) {
		return movieRepository.save(movie);
	}
	
}
