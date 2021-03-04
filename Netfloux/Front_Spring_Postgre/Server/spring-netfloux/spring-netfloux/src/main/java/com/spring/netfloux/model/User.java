/*package com.spring.netfloux.model;

import javax.persistence.Embeddable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "users")
public class User {
	
	private static final long serialVersionUID = 1L;
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int user_id;
	
	private String username;
	
	private String password;
	
	public User() {}
	
	public User(int user_id, String username, String password) {
		this.user_id=user_id;
		this.username = username;
		this.password = password;
	}
	
	public int getUser_id() {
		return user_id;
	}

	public void setUser_id(int user_id) {
		this.user_id = user_id;
	}
	
	public String getUser_username() {
		return username;
	}
	
	public void setUser_username(String username) {
		this.username=username;
	}
	
	public String getUser_password() {
		return password;
	}
	
	public void setUser_password(String password) {
		this.password=password;
	}
	
}
*/