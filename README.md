Best Buds API README

This project was created by Timothey Eakin & Sara West, Data Science students at Lambda School, in January 2021.

The Best Buds API is designed to enable legal users of cannabis to search through a list of potential strains and locate
five options which may meet their needs.

The front-end interface will supply a JSON object with one key-value pair: {user_input: "string typed by end user"}.

End users simply type in a sentence describing the medical complaints they hope to address by using cannabis.
They can include desired effects, flavors, and any other information they deem pertinent as well.

The api will return a JSON object containing information about the top five matching strains.
Keys: {name, description, effects, ailments}

Heroku https://best-buds-2020.herokuapp.com/

Dataset https://raw.githubusercontent.com/tt-dspt-200/best-buds/main/data/MJ.csv created by merging Kushy and Leafly datasets to create a more rubust body of information.

Product Vison Document https://docs.google.com/document/d/1cmrGMjtzMOi2HS8vJWKXRlwXgDXyYTlOVqk4AclTlhQ/edit?usp=sharing
