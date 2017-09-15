package com.shinesolutions;

import com.coxautodev.graphql.tools.SchemaParser;
import com.shinesolutions.graphqlpoc.service.Mutation;
import com.shinesolutions.graphqlpoc.service.Query;
import graphql.schema.GraphQLSchema;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class GraphPocApp {

    @Autowired
    private Query query;

    @Autowired
    private Mutation mutation;

    public static void main(String[] args) {
        SpringApplication.run(GraphPocApp.class, args);
    }

    @Bean
    GraphQLSchema schema(){
        return SchemaParser.newParser().file("schema.graphqls")
                .resolvers(query, mutation)
                .build()
                .makeExecutableSchema();
    }
}
