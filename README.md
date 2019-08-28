# Sellers.json Parser
A parser of sellers.json files

# About

According to the IAB Tech Lab:

```sellers.json provides a mechanism to enable buyers to discover who the entities are that are either direct sellers of or intermediaries in the selling of digital advertising.

A published and accessible sellers.json file allows the identity of the final seller of a bid request to be discovered (assuming that they are ads.txt authorized).  It also allows the identities of all nodes (entities that participated in the bid request) in the SupplyChain object to also be discovered.```

Once upon a time, an SSP / Network wouldn't want to disclose the publishers that they were working with, because that was seen as a competitive advantage. Now with sellers.json, there's a lot more transparency, which is great! This also allows publishers / adveritsers the ability to see the quality of publishers an SSP works with, or has direct access to sell on their behalf.

This script goes to a sellers.json endpoint (or several of them!) included in a dictionary inside the script, and outputs a single sellers.json file into an easy to read csv.

# Next steps

As adoption of sellers.json grows, I'll add additional exchanges / endpoints so we can get a comprehensive accounting of every sellers.json file in every exchange. 
