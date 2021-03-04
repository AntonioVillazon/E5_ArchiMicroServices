package com.spring.netfloux.model;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embeddable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/*
@Data
@AllArgsConstructor
@NoArgsConstructor
*/
@Entity
@Table(name = "movie_trailers")
public class Movie implements Serializable{


	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name="movie_id")
	private int movie_id;
	
	@Column(name="movie_name")
	private String movie_name;
	
	@Column(name="movie_url")
	private String movie_url;
	
	@Column(name="movie_synopsis")
	private String movie_synopsis;
	
	@Column(name="movie_image")
	private String movie_image;

	public Movie() { }	
	
	public Movie(int movie_id, String movie_name, String movie_url, String movie_synopsis, String movie_image) {
		this.movie_id = movie_id;
		this.movie_name = movie_name;
		this.movie_url = movie_url;
		this.movie_synopsis = movie_synopsis;
		this.movie_image = movie_image;
	}
	
	public int getMovie_id() {
		return movie_id;
	}

	public void setMovie_id(int movie_id) {
		this.movie_id = movie_id;
	}

	public String getMovie_name() {
		return movie_name;
	}

	public void setMovie_name(String movie_name) {
		this.movie_name = movie_name;
	}

	public String getMovie_url() {
		return movie_url;
	}

	public void setMovie_url(String movie_url) {
		this.movie_url = movie_url;
	}

	public String getMovie_synopsis() {
		return movie_synopsis;
	}

	public void setMovie_synopsis(String movie_synopsis) {
		this.movie_synopsis = movie_synopsis;
	}

	public String getMovie_image() {
		return movie_image;
	}

	public void setMovie_image(String movie_image) {
		this.movie_image = movie_image;
	}
	
	@Override
	public String toString() {
		String movieToString = "Movie{" + 
							   "movie_id" + movie_id +
							   ", movie_name" + movie_name +
							   ", movie_url" + movie_url +
							   ", movie_synopsis" + movie_synopsis +
							   ", movie_image" + movie_image +
							   "}";
		return movieToString;
	}
	
}
