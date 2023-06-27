# Garden Planner API

## R1

A few years ago, I started planning and establishing my first garden in the beautiful Southern Highlands of New South Wales, Australia. As enjoyable and rewarding as the experience was, I was quickly overwhelmed by how I was possibly going to manage it in the long term. I set up repeating monthly, quarterly and even yearly reminders across multiple applications, wrote notes and even resorted to putting all the plant slips in a zip lock bag! Fast forward a few months or even years and I never felt like I was in control, knowing what plants needed what and when. This organisational problem was only exacerbated as new plants were added and older plants removed.

The Garden Planner API was built using Flask to solve the problem of a person not being able to keep track of all of their trees and/or plants. It aims to be a central repository for a user to log details about the plants and trees they have in their outdoor and indoor spaces. It abides by full CRUD functionality by enabling the user to:

- Create new entries/records for the plants or trees they obtain with attributes for name, the plant's preferred location, the watering and fertilisation rates, as well as a space for additonal comments.
- Create areas where plants/trees belong, as well as spaces within those areas. For example, a user's "Backyard" area might contain multiple spaces or gardens.
- Access entries they have entered in order to be reminded about a plant's upkeep.
- Update plant records at any point.
- Delete plant records at any point.

This CRUD functionality helps the user to stay organised and in control of their garden planning and maintenance.

## R2

There are a number of reasons why the Garden Planner application was built and has a genuine need:

- The Garden Planner API simplifies and unifies the process of plant and tree record keeping. For me personally, I was finding it overwhelming managing how to log when I had last watered, fertilised, transplanted or repotted my plants and I was finding that I was "solving" this problem by logging reminders in different applications, keeping tab of the plant information slips coming back with the plant from a nursery, or simply just having to look and see what the plant was requiring at any given moment. This method of garden management was cumbersome and it was difficult to maintain accuracy and a method of record-keeping. The simple process of entering data in fields such as plants and planting spaces allows for the user to keep tab of their plant varieties in a single, organised location.
- The application does not prefill the data entry fields with irrelevant information about plant upkeep from other countries with different climates to Australia. The user can enter accurate and relevant information, often obtained by simply looking over the slip that comes with each plant.
- The user can tailor the application to their needs, making it as simple or detailed as they need. It's designed to be flexible, allowing the user to input data that reflects their space. This solves the problem identied in R1 above by giving the user an opportunity to record all their plant species and planting locations in an organised manner.
- As our gardens change and update, the Garden Planner API allows for full CRUD functionality across the various entities. This solves the problem of not being able to easily remmeber how to care for our gardens as they grow.