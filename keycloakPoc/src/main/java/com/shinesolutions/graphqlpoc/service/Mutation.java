package com.shinesolutions.graphqlpoc.service;

import com.coxautodev.graphql.tools.GraphQLMutationResolver;
import com.shinesolutions.graphqlpoc.dto.Link;
import com.shinesolutions.graphqlpoc.dao.LinkRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class Mutation implements GraphQLMutationResolver {

    private final LinkRepository linkRepository;

    @Autowired
    public Mutation(LinkRepository linkRepository) {
        this.linkRepository = linkRepository;
    }

    public Link createLink(String url, String description){
        Link newLink = new Link(url, description);
        linkRepository.save(newLink);

        return newLink;
    }
}
