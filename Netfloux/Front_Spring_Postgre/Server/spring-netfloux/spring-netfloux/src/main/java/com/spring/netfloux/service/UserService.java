/*package com.spring.netfloux.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;

import com.spring.netfloux.model.User;
import com.spring.netfloux.repository.UserRepository;

@Service
public class UserService {

	private final UserRepository userRepository;
	
	@Autowired
	public UserService(UserRepository userRepository) {
		this.userRepository = userRepository;
	}
	
	@GetMapping("/")
	public String login() {
		return "authenticated successfully";
	}
	
	
	@GetMapping("/getUsers")
	public List<User> getUsers(){
		return userRepository.findAll();
	}
	

}
*/