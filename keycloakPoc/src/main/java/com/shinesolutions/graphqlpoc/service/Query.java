package com.shinesolutions.graphqlpoc.service;

import com.coxautodev.graphql.tools.GraphQLQueryResolver;
import com.shinesolutions.graphqlpoc.dto.Link;
import com.shinesolutions.graphqlpoc.dao.LinkRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class Query implements GraphQLQueryResolver {

    private final LinkRepository linkRepository;

    @Autowired
    public Query(LinkRepository linkRepository) {
        this.linkRepository = linkRepository;
    }

    public List<Link> allLinks(){
        return linkRepository.findAll();
    }
}