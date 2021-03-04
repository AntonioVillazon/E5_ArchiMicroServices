package com.spring.netfloux;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;

@SpringBootApplication(scanBasePackages={"com.spring.netfloux"})
public class SpringNetflouxApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringNetflouxApplication.class, args);
	}

}
