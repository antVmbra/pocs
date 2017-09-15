package com.shinesolutions.graphqlpoc.dao;

import com.shinesolutions.graphqlpoc.dto.Link;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface LinkRepository extends MongoRepository<Link, String> {
}
