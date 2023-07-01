# Garden Planner API

## R1 - Problem Identification

A few years ago, I started planning and establishing my first garden in the beautiful Southern Highlands of New South Wales, Australia. As enjoyable and rewarding as the experience was, I was quickly overwhelmed by how I was possibly going to manage it in the long term. I set up repeating monthly, quarterly and even yearly reminders across multiple applications, wrote notes and even resorted to putting all the plant slips in a zip lock bag! Fast forward a few months or even years and I never felt like I was in control, knowing what plants needed what and when. This organisational problem was only exacerbated as new plants were added and older plants removed.

The Garden Planner API was built using Flask to solve the problem of a person not being able to keep track of all of their trees and/or plants. It aims to be a central repository for a user to log details about the plants and trees they have in their outdoor and indoor spaces. It abides by full CRUD functionality by enabling the user to:

- Create new entries/records for the plants or trees they obtain with attributes for name, the plant's preferred location, the watering and fertilisation rates, as well as a space for additional comments.
- Create areas where plants/trees belong, as well as spaces within those areas. For example, a user's "Backyard" area might contain multiple spaces or gardens.
- Access entries they have entered in order to be reminded about a plant's upkeep.
- Update plant records at any point.
- Delete plant records at any point.

This CRUD functionality helps the user to stay organised and in control of their garden planning and maintenance.

## R2 - Problem Justification

There are a number of reasons why the Garden Planner application was built and has a genuine need:

- The Garden Planner API simplifies and unifies the process of plant and tree record keeping. For me personally, I was finding it overwhelming managing how to log when I had last watered, fertilised, transplanted or repotted my plants and I was finding that I was "solving" this problem by logging reminders in different applications, keeping tab of the plant information slips coming back with the plant from a nursery, or simply just having to look and see what the plant was requiring at any given moment. This method of garden management was cumbersome and it was difficult to maintain accuracy and a method of record-keeping. The simple process of entering data in fields such as plants and planting spaces allows for the user to keep tab of their plant varieties in a single, organised location.
- The application does not prefill the data entry fields with irrelevant information about plant upkeep from other countries with different climates to Australia. The user can enter accurate and relevant information, often obtained by simply looking over the slip that comes with each plant.
- The user can tailor the application to their needs, making it as simple or detailed as they need. It's designed to be flexible, allowing the user to input data that reflects their space. This solves the problem identified in R1 above by giving the user an opportunity to record all their plant species and planting locations in an organised manner.
- As our gardens change and update, the Garden Planner API allows for full CRUD functionality across the various entities. This solves the problem of not being able to easily remember how to care for our gardens as they grow.

## R3 - Evaluation of Relational Databases and PostgreSQL

### Relational Databases

According to IBM, database management systems (DBMS) are categorised according to their data structures or types, with common examples being:

- inverted list,
- hierarchic,
- network, and
- relational (*What is a database management system?*).

Using a DBMS for the Garden Planner API has allowed for a full suite of data manipulation tools (DML) as well as tools for management of the database structure itself (DDL). There are many distinct advantages to DBMS, in general, including:

- easier data handling,
- security and privacy,
- a reduction in data inconsistency and redundancy,
- ease of use, and
- abstraction (/Advantages of Database Management System/).

However, DBMS do differ and each system has advantages and disadvantages. A hierarchical model, for example, would be well suited to data that stays relatively static. However, this Garden Planner API requires a dynamism in its data structures as well as its data.

Given this, and after careful consideration, it was decided that a relational database management system was the most advantageous choice for the Garden Planner API. The primary reason for this decision was that this form of DBMS provides the ability to join tables together, therefore showing a relationship between data or how tables connect (*Benefits of relational databases*). The API needs to solve an organisational problem for its users as identified in R1 and R2 above. Given this, an organised solution to data storage, as exemplified through relational DBMS, allows the user to see the relationships between entities. For example, the user can log details of plant species in their garden (`PlantRecords`), and as the garden develops, they can add instances of this `plantrecord` in another entity (`Plants`). These `plants` can belong to multiple `spaces` and these `spaces` can be contained within `areas`. In a DBMS like PostgreSQL, entities/tables can be easily through Structured Query Language (SQL) and populated with data through queries.

Using a relational DBMS also assists the user in eliminating redundancies. This is primarily achieved through a process known as data normalisation. Normalisation is the process of creating tables and table relationships that make the database flexible or alterable, eliminating redundancies and inconsistent dependencies (*Description of the database normalization basics*). To illustrate, if the Garden Planner database stored data regarding plants in multiple tables in the database, maintaining this information would be tedious and error prone. This data should only be located in one table and this process of normalising data is achieved through a three-step process of 1NF, 2NF and 3NF.

In a relational DBMS, data structure is predefined and table-based. This might be a disadvantage compared to the greater freedoms provided in non-relational databases to represent data in key-value pairs, documents, column-families or graphs, however, tables are an apt solution for the data collected in this instance.

Relational DBMS may be slower in performance in some use cases; however, big data and real-time processing were not required for this application. Indeed, relational DBMS do have more limited scalability than non-relational databases, but at this stage of the development process, this is not a concern. 

### PostgreSQL

PostgreSQL was chosen for the Garden Planner API because it is a ubiquitous relational DBMS used with Flask applications that is open-source. This makes it a free application that brings with it the freedom to use, modify and implement it to suit business needs (*What is PostgreSQL?*). Additionally, PostgreSQL supports a range of features, including support for:

- writing database functions in a range of languages, including Python, JavaScript and Shell;
- a large number of data types from basic types such as numeric and string, geometric types, JSON, monetary types, dates and arrays. PostgreSQL also allows the user to define their own complex data types (*The benefits of PostgreSQL*);
- full-text search;
- a variety of business sizes and needs as a result of its robust authentication, access control and privilege management systems (*The benefits of PostgreSQL*);
- views, for information that is often queried;
- attaching comments; and
- write-ahead logging so the data can be recovered after a software crash.

Like most other relational DBMS, PostgreSQL allows the user to store data in tables and query, modify and retrieve that data using relational algebra techniques through structured query language (SQL); however, PostgreSQL is technically an Object-Relational DBMS, meaning it has some additional functionality (*The benefits of PostgreSQL*). This includes defining complex data types, inheritance and overloading functions (*The benefits of PostgreSQL*).

PostgreSQL has a large and active community of users and is well-supported with documentation and help guides.

Despite the numerous advantages listed above, PostgreSQL is comparatively slower than other DBMS such as MySQL. Additionally, not all open source applications support it. As it is open source and managed by many, compatibility and version update issues may arise.

## R4 - Functionality and Benefits of an Object Relational Mapper (ORM)

An Object Relational Mapper (ORM) acts as a bridge between object-oriented programs and relational databases. In practice and directly related to this API, this means that an ORM will convert Python objects to the relational schema of the database. Direct SQL queries for the CRUD operations are therefore not needed when using an ORM as it acts as an additional layer between a programming language and a database. Principally, this means that it standardises the coding process, reducing boilerplate and speeding development time (*Understanding Object-Relational Mapping*). This API, in particular, has used the SQLAlchemy ORM which provides SQL functionality, and efficient and high-performing database access, adapted into a simple and Pythonic domain language (*The Python SQL Toolkit and Object Relational Mapper*).

SQLAlchemy provides extensive help documentation for understanding its comprehensive functionality. It has allowed the following functionality with this API:

- Declarative mapping of models which simultaneously define a Python object model as well as database metadata that describes real SQL tables that exist, or will exist, in a database (*SQLAlchemy 2.0 Documentation*). In this API, a model has been created for each entity in the database.
- Creating instances of classes, using the `session.add_all()` method to add multiple objects at once, and then using the `session.commit() method to flush any pending changes and commit the current database transaction (*SQLAlchemy 2.0 Documentation*).
- Using the `select()` function to create a new `Select` object, then invoked using a `Session`.
- Using the `Session.scalars()` method to return a `ScalarResult` to iterate through the ORM objects selected.
- Querying against multiple tables at once using the join keyword in the `Select.join()` method.
- Automatically tracking changes to the objects as they are made.

## R5 - Endpoint Documentation

### Auth Routes

#### `/auth/register`

- HTTP Request Verb: POST
- Description: Allows a new user to register their first name, last name, email and password and create an account with the Garden Planner application. This data is added to the `users` database entity.
- Required Data: 'f_name', 'l_name', 'email', 'password'
- Authentication Methods: None

The following is the expected response from the `auth/register` endpoint using sample data:

![Register](docs/register.png)

#### `/auth/login`

- HTTP Request Verb: POST
- Description: Allows a new user to login with their registered credentials. The response is a JWT token and user summary, excluding password.
- Required Data: 'email', 'password'
- Authentication Methods: A JWT token is returned to the server for authentication and authorisation purposes.

The following is the expected response from the `auth/login` endpoint using sample data:

![Login](docs/login.png)

#### `/auth/users`

- HTTP Request Verb: GET
- Description: Allows a user with admin credentials to obtain a JSON list of all registered users. The server response includes nested data regarding areas owned by those users.
- Required Data: 'email', 'password'
- Authentication Methods: `@jwt_required()`, `admin_required()`

The following is the expected response from the `auth/users` endpoint using sample data:

```
[
  {
    "areas": [
      {
        "is_indoor": false,
        "is_outdoor": true,
        "name": "Frontyard"
      },
      {
        "is_indoor": false,
        "is_outdoor": true,
        "name": "Backyard"
      }
    ],
    "email": "14209@coderacademy.edu.au",
    "f_name": "Joshua",
    "l_name": "Davis"
  },
  {
    "areas": [
      {
        "is_indoor": true,
        "is_outdoor": false,
        "name": "House"
      }
    ],
    "email": "neilarmstrong@gmail.com",
    "f_name": "Neil",
    "l_name": "Armstrong"
  },
  {
    "areas": [],
    "email": "donaldtrump@gmail.com",
    "f_name": "Donald",
    "l_name": "Trump"
  }
]
```

#### `/auth/users/<int:user_id>`

- HTTP Request Verb: GET
- Description: Allows a user with admin credentials to obtain a single record for the specified user in the URI using their user ID. The server response includes nested data regarding areas and spaces owned by that user.
- Required Data: 'email', 'password'
- Authentication Methods: `@jwt_required()`, `admin_required()`

The following is the expected response from the `/users/<int:user_id>` endpoint using sample data:

```
{
  "areas": [
    {
      "is_indoor": false,
      "is_outdoor": true,
      "name": "Frontyard"
    },
    {
      "is_indoor": false,
      "is_outdoor": true,
      "name": "Backyard"
    }
  ],
  "email": "14209@coderacademy.edu.au",
  "f_name": "Joshua",
  "l_name": "Davis",
  "spaces": [
    {
      "area": {
        "is_indoor": false,
        "is_outdoor": true,
        "name": "Frontyard"
      },
      "area_id": 1,
      "name": "Rose Garden"
    },
    {
      "area": {
        "is_indoor": true,
        "is_outdoor": false,
        "name": "House"
      },
      "area_id": 3,
      "name": "Kitchen"
    }
  ]
}

```

#### `/auth/users/<int:user_id>`

- HTTP Request Verb: DELETE
- Description: Allows a user with admin credentials to delete a user from the database.
- Required Data: 'email', 'password'
- Authentication Methods: `@jwt_required()`, `admin_required()`

The following is the expected response from the `/users/<int:user_id>` endpoint using sample data: `{}` and error code `200`.

![DeleteUser](docs/deleteuser.png)

### Area Routes

#### `/areas`

- HTTP Request Verb: GET
- Description: Allows a logged in user to access a list of all areas, nested with associated users and spaces.
- Required Data: None
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/areas` endpoint using sample data:

```
[
  {
    "id": 2,
    "is_indoor": false,
    "is_outdoor": true,
    "name": "Backyard",
    "spaces": [
      {
        "name": "Vegetable Garden"
      }
    ],
    "user": {
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis"
    }
  },
  {
    "id": 1,
    "is_indoor": false,
    "is_outdoor": true,
    "name": "Frontyard",
    "spaces": [
      {
        "name": "Rose Garden"
      },
      {
        "name": "Window Garden"
      }
    ],
    "user": {
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis"
    }
  },
  {
    "id": 3,
    "is_indoor": true,
    "is_outdoor": false,
    "name": "House",
    "spaces": [
      {
        "name": "Living Room"
      },
      {
        "name": "Kitchen"
      }
    ],
    "user": {
      "email": "neilarmstrong@gmail.com",
      "f_name": "Neil",
      "l_name": "Armstrong"
    }
  }
]
```

#### `/areas/outdoors`

- HTTP Request Verb: GET
- Description: Allows a logged in user to access a list of all outdoor areas, nested with associated users and spaces.
- Required Data: None
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/areas/outdoors` endpoint using sample data:

```
[
  {
    "id": 1,
    "is_indoor": false,
    "is_outdoor": true,
    "name": "Frontyard",
    "spaces": [
      {
        "name": "Rose Garden"
      },
      {
        "name": "Window Garden"
      }
    ],
    "user": {
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis"
    }
  },
  {
    "id": 2,
    "is_indoor": false,
    "is_outdoor": true,
    "name": "Backyard",
    "spaces": [
      {
        "name": "Vegetable Garden"
      }
    ],
    "user": {
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis"
    }
  }
]
```

#### `/areas/<int:area_id>`

- HTTP Request Verb: GET
- Description: Allows a logged in user to access a single area by specifying its ID in the URI.
- Required Data: None
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/areas/<int:area_id` endpoint using sample data:

![GetArea](docs/area.png)

#### `/areas`

- HTTP Request Verb: POST
- Description: Allows a logged in user to create a new area
- Required Data: 'name', 'is_outdoor', 'is_indoor'
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/areas` endpoint using sample data:

![CreateArea](docs/createarea.png)

#### `/areas/<int:area_id>`

- HTTP Request Verb: PUT, PATCH
- Description: Allows a logged in user to update an existing area
- Required Data: any to-be-updated fields
- Authentication Methods: `@jwt_required()`, `@admin_or_owner_required()`

The following is the expected response from the `/areas/<int:area_id` endpoint using sample data:

![UpdateArea](docs/updatearea.png)

#### `/areas/<int:area_id>`

- HTTP Request Verb: DELETE
- Description: Allows a logged in user to delete an existing area
- Required Data: None
- Authentication Methods: `@jwt_required()`, `@admin_or_owner_required()`

The following is the expected response from the `/areas/<int:area_id` endpoint using sample data:

![DeleteArea](docs/deletearea.png)

### Space Routes

#### `/spaces`

- HTTP Request Verb: GET
- Description: Allows a logged in user to access a list of all spaces, nested with associated areas.
- Required Data: None
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/spaces` endpoint using sample data:

```
[
  {
    "area": {
      "is_indoor": true,
      "is_outdoor": false,
      "name": "House"
    },
    "area_id": 3,
    "id": 4,
    "name": "Kitchen",
    "user": {
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis"
    }
  },
  {
    "area": {
      "is_indoor": true,
      "is_outdoor": false,
      "name": "House"
    },
    "area_id": 3,
    "id": 3,
    "name": "Living Room",
    "user": {
      "email": "donaldtrump@gmail.com",
      "f_name": "Donald",
      "l_name": "Trump"
    }
  },
  {
    "area": {
      "is_indoor": false,
      "is_outdoor": true,
      "name": "Frontyard"
    },
    "area_id": 1,
    "id": 1,
    "name": "Rose Garden",
    "user": {
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis"
    }
  },
  {
    "area": {
      "is_indoor": false,
      "is_outdoor": true,
      "name": "Backyard"
    },
    "area_id": 2,
    "id": 5,
    "name": "Vegetable Garden",
    "user": {
      "email": "neilarmstrong@gmail.com",
      "f_name": "Neil",
      "l_name": "Armstrong"
    }
  },
  {
    "area": {
      "is_indoor": false,
      "is_outdoor": true,
      "name": "Frontyard"
    },
    "area_id": 1,
    "id": 2,
    "name": "Window Garden",
    "user": {
      "email": "neilarmstrong@gmail.com",
      "f_name": "Neil",
      "l_name": "Armstrong"
    }
  }
]
```

#### `/spaces/<int:space_id>`

- HTTP Request Verb: GET
- Description: Allows a logged in user to access a single space by specifying its ID in the URI.
- Required Data: None
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/spaces/<int:space_id>` endpoint using sample data:

![GetSpace](docs/space.png)

#### `/spaces`

- HTTP Request Verb: POST
- Description: Allows a logged in user to create a new space
- Required Data: 'name', 'area_id'
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/spaces` endpoint using sample data:

![CreateSpace](docs/createspace.png)

#### `/spaces/<int:space_id>`

- HTTP Request Verb: PUT, PATCH
- Description: Allows a logged in user to update an existing space
- Required Data: any to-be-updated fields
- Authentication Methods: `@jwt_required()`, `admin_or_owner_required()`

The following is the expected response from the `/spaces/<int:space_id>` endpoint using sample data:

![UpdateSpace](docs/updatespace.png)

#### `/spaces/<int:space_id>`

- HTTP Request Verb: DELETE
- Description: Allows a logged in user to delete an existing space
- Required Data: None
- Authentication Methods: `@jwt_required()`, `admin_or_owner_required()`

The following is the expected response from the `/spaces/<int:space_id>` endpoint using sample data:

![DeleteSpace](docs/deletespace.png)

### PlantRecord Routes

#### `/plantrecords`

- HTTP Request Verb: GET
- Description: Allows a logged in user to access a list of all plantrecords, nested with associated areas, spaces and plants.
- Required Data: None
- Authentication Methods: `@jwt_required()`, `admin_required`

The following is the expected response from the `/plantrecords` endpoint using sample data:

```
[
  {
    "description": "Camellias are attractive evergreen shrubs with a variety of flower colours.",
    "fertilisation_rate": "Key feeding times are autumn as buds are developing and in spring once flowering has finished.",
    "id": 1,
    "name": "Camellia",
    "other_comments": "Keep the plant moist but well-drained.",
    "plants": [
      {
        "date_fertilised": null,
        "date_planted": null,
        "id": 1,
        "space_id": 1
      }
    ],
    "preferred_location": "Partial sun",
    "user": {
      "areas": [
        {
          "is_indoor": false,
          "is_outdoor": true,
          "name": "Frontyard"
        },
        {
          "is_indoor": false,
          "is_outdoor": true,
          "name": "Backyard"
        }
      ],
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis",
      "spaces": [
        {
          "area": {
            "is_indoor": false,
            "is_outdoor": true,
            "name": "Frontyard"
          },
          "area_id": 1,
          "name": "Rose Garden"
        },
        {
          "area": {
            "is_indoor": true,
            "is_outdoor": false,
            "name": "House"
          },
          "area_id": 3,
          "name": "Kitchen"
        }
      ]
    },
    "water_rate": "Average"
  },
  {
    "description": "A large-flowered hybrid plant cultivated as a garden flower.",
    "fertilisation_rate": "Use a controlled release fertiliser when planting.",
    "id": 2,
    "name": "Pansy",
    "other_comments": "Keep the plant moist but well-drained.",
    "plants": [
      {
        "date_fertilised": null,
        "date_planted": null,
        "id": 2,
        "space_id": 1
      }
    ],
    "preferred_location": "Partial sun",
    "user": {
      "areas": [
        {
          "is_indoor": false,
          "is_outdoor": true,
          "name": "Frontyard"
        },
        {
          "is_indoor": false,
          "is_outdoor": true,
          "name": "Backyard"
        }
      ],
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis",
      "spaces": [
        {
          "area": {
            "is_indoor": false,
            "is_outdoor": true,
            "name": "Frontyard"
          },
          "area_id": 1,
          "name": "Rose Garden"
        },
        {
          "area": {
            "is_indoor": true,
            "is_outdoor": false,
            "name": "House"
          },
          "area_id": 3,
          "name": "Kitchen"
        }
      ]
    },
    "water_rate": "Average"
  }
]
```

#### `/plantrecords/<int:plantrecord_id>`

- HTTP Request Verb: GET
- Description: Allows a logged in user to access a single plantrecord by specifying its ID in the URI.
- Required Data: None
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/plantrecords/<int:plantrecord_id>` endpoint using sample data:

```
{
  "description": "Camellias are attractive evergreen shrubs with a variety of flower colours.",
  "fertilisation_rate": "Key feeding times are autumn as buds are developing and in spring once flowering has finished.",
  "id": 1,
  "name": "Camellia",
  "other_comments": "Keep the plant moist but well-drained.",
  "plants": [
    {
      "date_fertilised": null,
      "date_planted": null,
      "id": 1,
      "space_id": 1
    }
  ],
  "preferred_location": "Partial sun",
  "user": {
    "areas": [
      {
        "is_indoor": false,
        "is_outdoor": true,
        "name": "Frontyard"
      },
      {
        "is_indoor": false,
        "is_outdoor": true,
        "name": "Backyard"
      }
    ],
    "email": "14209@coderacademy.edu.au",
    "f_name": "Joshua",
    "l_name": "Davis",
    "spaces": [
      {
        "area": {
          "is_indoor": false,
          "is_outdoor": true,
          "name": "Frontyard"
        },
        "area_id": 1,
        "name": "Rose Garden"
      },
      {
        "area": {
          "is_indoor": true,
          "is_outdoor": false,
          "name": "House"
        },
        "area_id": 3,
        "name": "Kitchen"
      }
    ]
  },
  "water_rate": "Average"
}
```

#### `/plantrecords`

- HTTP Request Verb: POST
- Description: Allows a logged in user to create a new plantrecord
- Required Data: 'name'
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/plantrecords` endpoint using sample data:

![CreatePlantRecord](docs/createplantrecord.png)

#### `/plantrecords/<int:plantrecord_id>`

- HTTP Request Verb: PUT, PATCH
- Description: Allows a logged in user to update an existing plantrecord
- Required Data: any to-be-updated fields
- Authentication Methods: `@jwt_required()`, `admin_or_owner_required()`

The following is the expected response from the `/plantrecords/<int:plantrecord_id>` endpoint using sample data:

![UpdatePlantRecord](docs/updateplantrecord.png)

#### `/plantrecords/<int:plantrecord_id>`

- HTTP Request Verb: DELETE
- Description: Allows a logged in user to delete an existing plantrecord
- Required Data: None
- Authentication Methods: `@jwt_required()`, `admin_or_owner_required()`

The following is the expected response from the `/plantrecords/<int:plantrecord_id>` endpoint using sample data:

![DeletePlantRecord](docs/deleteplantrecord.png)

### Plant Routes

#### `/plants`

- HTTP Request Verb: GET
- Description: Allows a logged in user to access a list of all plants with their associated plantrecord
- Required Data: None
- Authentication Methods: `@jwt_required()`, `admin_required`

The following is the expected response from the `/plantrecords` endpoint using sample data:

```
[
  {
    "date_fertilised": null,
    "date_planted": null,
    "id": 1,
    "plantrecord": {
      "fertilisation_rate": "Key feeding times are autumn as buds are developing and in spring once flowering has finished.",
      "name": "Camellia",
      "other_comments": "Keep the plant moist but well-drained.",
      "preferred_location": "Partial sun",
      "water_rate": "Average"
    },
    "plantrecord_id": 1,
    "space_id": 1,
    "user": {
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis"
    },
    "user_id": 1
  },
  {
    "date_fertilised": null,
    "date_planted": null,
    "id": 2,
    "plantrecord": {
      "fertilisation_rate": "Use a controlled release fertiliser when planting.",
      "name": "Pansy",
      "other_comments": "Keep the plant moist but well-drained.",
      "preferred_location": "Partial sun",
      "water_rate": "Average"
    },
    "plantrecord_id": 2,
    "space_id": 1,
    "user": {
      "email": "14209@coderacademy.edu.au",
      "f_name": "Joshua",
      "l_name": "Davis"
    },
    "user_id": 1
  }
]

```

#### `/plants/<int:plant_id>`

- HTTP Request Verb: GET
- Description: Allows a logged in user to access a single plant by specifying its ID in the URI.
- Required Data: None
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/plants/<int:plant_id>` endpoint using sample data:

![Plant](docs/plant.png)

#### `/plants`

- HTTP Request Verb: POST
- Description: Allows a logged in user to create a new plant instance
- Required Data: 'plantrecord_id', 'space_id'
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/plants` endpoint using sample data:

![CreatePlant](docs/createplant.png)

#### `/plants/<int:plant_id>`

- HTTP Request Verb: PUT, PATCH
- Description: Allows a logged in user to update an existing plant
- Required Data: any to-be-updated fields
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/plants/<int:plant_id>` endpoint using sample data:

![UpdatePlantRecord](docs/updateplantrecord.png)

#### `/plants/<int:plant_id>`

- HTTP Request Verb: DELETE
- Description: Allows a logged in user to delete an existing plant
- Required Data: None
- Authentication Methods: `@jwt_required()`

The following is the expected response from the `/plants/<int:plant_id>` endpoint using sample data:

![DeletePlant](docs/deleteplant.png)

## R6 - Entity Relationship Diagram (ERD)

![ERD](docs/erd.png)  

## R7 - Third Party Services

The following third party services were used in the development of the Garden Planner API. It is important to note initially that Flask was used as the Python web framework to build the application. Flask is considered a microframework as it is designed to keep the core of the application simple and scalable. Flask supports multiple library extensions to add capabilities to any application. The benefits of Flask, however, include automation, accessibility and reusability.

### SQLAlchemy (version 2.0.16)

SQLAlchemy is a popular Python SQL toolkit and ORM that gave me the full power and flexibility of SQL and the PostgreSQL relational database. It provides a Pythonic way of interacting with databases so you can more efficiently query your data. It allows for Python classes or objects to be mapped to the database, thereby allowing the object model and database schema to develop in a decoupled manner (*SQLAlchemy Tutorial*). An additional benefit of using an ORM such as SQLAlchemy is that it is able to sanitise the incoming data in its translation of the database query to SQL.

### Psycopg2 (version 2.9.6)

Psychopg2 is the most popular PostgreSQL database adapter for Python. As the ORM used for this API, SQLAlchemy, is database agnostic, it needed an adapter to interact with the database. It is written in C and enables the user to perform the full range of SQL operations against a PostgreSQL database.

### Flask-Marshmallow (version 0.15.0)

Flask-Marshmallow is a framework-agnostic library for converting complex data types, such as Python classes, into another type, such as JSON. Marshmallow schemas have been used for every model in the Garden Planner API to validate input data, deserialize input data and serialize app-level objects to Python types so they can then be rendered to standard formats such as JSON (*marshmallow: simplified object serialization*). It is important to note that loading data from any request is known as deserialization, but the process of formatting the output response data is known as serialization, where data is dumped to the response (*Data Schema*).

### python-dotenv (version 1.0.0)

The directory for the API includes a `.env` file that is also placed in the `.gitignore` file. This `.env` file lists a number of sensitive key-value pairs relating to the database URI and the JWT Secret Key. The python-dotenv package reads these values and sets them up as environment variables, preventing them from needing to be hard-coded and potentially compromised. Placing them into the `.gitignore` file ensures they are protected, but any developer can read the `.env.sample` file to know what the variables are named.

The directory also contains a `flaskenv` file that similarly is used to set up Flask-specific environment variables such as the name of the application's main file and function, what port to use, as well as whether to run the application in de-bug mode.

### Flask-Bcrypt (version 1.0.1)

Flask-Bcrypt is an extension for Flask used to protect user passwords using bcrypt hashing. Hashing is the process whereby plaintext passwords are converted into hashed or encrypted formats that cannot be easily reverse-engineered, and bcrypt is simply a popular hashing algorithm based on the Blowfish cipher which is designed to be slow and computationally expensive (*Password Hashing with Bcrypt in Flask*). This makes it more difficult for attackers to crack passwords.

Changing even one character in the plaintext password will drastically change the resulting hashed password.

```
password = bcrypt.generate_password_hash(user_info['password']).decode('utf-8')
```

### Flask-JWT-Extended (version 4.5.2)

The Flask-JWT-Extended extension is used in the application to make JSON Web Tokens and authenticate users. JWT is able to verify the user's email and password when entered and sends back an encrypted token in the following form:

```
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODIxNDM3NSwianRpIjoiNzNjYTI3Y2MtMjIwZi00NDJhLTg0NGQtMDhlZTNiY2UyYmE2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjg4MjE0Mzc1LCJleHAiOjE2ODgzMDA3NzV9.VFRrfk7C-PNPI5WaRWv8u0X4TKTagtj6XPcEw0UOz78",
  "user": {
    "email": "14209@coderacademy.edu.au",
    "f_name": "Joshua",
    "l_name": "Davis"
  }
}
```

In its simplest form, this extension facilitates the use of `create_access_token` to to make JSON Web Tokens, `jwt_required()` to protect endpoint routes, and `get_jwt_identity()` to get the identity of a JWT in a protected route. The generated token prevents the need for a user needing to constantly login at each request. The token needs to be added to the authorization header for each further request. A user's identity can be extracted from the JWT token, allowing the API to serve resources to specific users.

## R8 - Model Description

All of the models for the API are available within a `models` directory and are built using the ORM, SQLAlchemy. These models provide an abstract representation of the tables to be implemented in the database, where each model is a Python class or object, for example `class Area(db.Model)`. Each attribute of the model in question represents a column in the database table and each class inherits from `db.Model`. These models directly and exactly correlate with the ERD created for the API.

In the `init.py` file, the `db` instance is created using SQLAlchemy. In turn, each of the five models in the API inherits from `db.Model` which helps the controller receive the information it needs from the database. The models each define column names, data types, constraints, primary keys and foreign keys. This is a Pythonic representation of SQL queries that interacts with the database schema in a seamless manner.

### The `user` model

The `user` model is firstly given the syntactically correct `users` plural `__tablename__`. A number of class attributes are then defined as the columns of the table. A primary key of `id` is first established, followed by attributes for `f_name`, `l_name`, `email`, `password` and `is_admin`. The data types for each attribute are defined and a few constraints are outlined, including the fact that the `email` must be provided and must be unique from other entries in the table, the `password` field must be provided, and the `is_admin` Boolean defaults to `False` if no value is entered.

After this, a number of `db.relationships` are defined, all of which back populate to the variable, `users`. These four relationships are established here because the `user_id` attribute is referenced as a foreign key by all other models in the database. This is due to the fact that users can:

1. Create, read, edit and delete areas
1. Create, read, edit and delete spaces
1. Create, read, edit and delete plantrecords
1. Create, read, edit and delete plants

The `db.relationship` entries specified here allow for the `UserSchema` to nest information about the tables and data in which the `user_id` is a foreign key.

The Marshmallow `UserSchema` validates input data, deserialises input data to app-level objects and serialises app-level objects to primitive Python types (*marshmallow: simplified object serialization*). In essence, this `UserSchema` converts the Python class, `User`, into a JSONified data type.

### The `area` model

The `area` model is firstly given the syntactically correct `areas` plural `__tablename__`. A number of class attributes are then defined as the columns of the table. A primary key of `id` is first established, followed by attributes for `name`, `is_outdoor` and `is_indoor`. The data types for each attribute are defined.

A `db.ForeignKey` is setup to link the table to `users.id` which is a mandatory field. This means that an `area` can only be created by a user as the `user` owns or establishes or defines the `area`. 

After this, a number of `db.relationships` are defined, all of which back populate to the variable, `areas`. These two relationships are established here because the class has a relationship with the `User` class due to the foreign key, `user_id`, and to the `Space` class as it references `area_id` as a foreign key. This allows for a two-way relationship between the classes where each can reference each other in their respective Schemas and nested data.

The `db.relationship` entries specified here allow for the `AreaSchema` to nest information about the tables and data specified under `class Meta`.

The Marshmallow `AreaSchema` includes in-built validation methods, including that the `name` attribute given to an `Area` must be a minimum length of 3 characters and can only contain characters specified in `Regexp`. A custom error message is provided if the user enters an invalid `name`. In essence, this `AreaSchema` converts the Python class, `Area`, into a JSONified data type.

### The `space` model

The `space` model is firstly given the syntactically correct `spaces` plural `__tablename__`. This model only contains one attribute, `name`, which is defined as a 100 character string.

Two `db.ForeignKey` are set up, including the foreign keys `area_id` and `user_id`. The `Space` model is in a one to many relationship with both `Area` and `User` in that:

1. A user can have many spaces, but a space can only belong to one user, and
1. An area can contain many spaces, but a space can only belong to one area.

There is also a `db.relationship` setup to both `User` and `Area` so that back population can occur in a two sided manner and, ultimately, the `SpaceSchema` can nest data from both these classes in the output to the server.

### The `plantrecord` model

The `plantrecord` model is firstly given the syntactically correct `plantrecords` plural `__tablename__`. A number of class attributes are then defined as the columns of the table. A primary key of `id` is first established, followed by attributes for `name`, `description`, `preferred_location`, `water_rate`, `fertilisation_rate` and `other_comments`. The data types for each attribute are defined and a few constraints are outlined in a similar fashion to previous models.

The only `db.ForeignKey` required is for `user_id` as a user can create many `plantrecords` but ultimately these records can only belong to one user, hence `plantrecord_id` is not needed as a foreign key in the `User` model.

Two `db.relationship` are setup so that back population can occur in a two sided manner and, ultimately, the `PlantRecordSchema` can nest data from both `User` and `Plant`.

The Marshmallow `PlantRecordSchema` includes in-built validation methods, including that the `name` is a certain minimum length and that `water_rate` is given one of a number of predefined one-word responses in `VALID_WATERRATES`. A custom decorator function is initiated if a valid `water_rate` is not selected. Additionally, the Schema provides a number of `load_default` fields if the user does not enter in anything, and in every case it is an empty string.

### The `plant` model

The `plant` model is firstly given the syntactically correct `plants` plural `__tablename__`. A number of class attributes are then defined as the columns of the table. A primary key of `id` is first established, followed by two `db.Date` data types for `date_planted` and `date_fertilised` both of which are not required of the user. Three `db.ForeignKey` are set up because:

1. A user can plant many plants, but a plant can only belong to one user,
1. A space can contain many plants, but a plant can only belong to one space, and 
1. A plant record can be associated with many instances of plants, but each plant can only correlate to one plant record.

For these reasons, foreign keys to `user_id`, `space_id` and `plantrecord_id` are defined.

Two `db.relationship` are setup so that back population can occur in a two sided manner and, ultimately, the `PlantSchema` can nest data from both `User` and `PlantRecord`. This is incredibly important as, without nested `PlantRecord` data, for example, the `Plant` data is relatively meaningless.

The Marshmallow `PlantSchema` validates input data, deserialises input data to app-level objects and serialises app-level objects to primitive Python types (*marshmallow: simplified object serialization*). In essence, this `PlantSchema` converts the Python class, `Plant`, into a JSONified data type.

## R9 - Database Relations

The Garden Planner API was built using a relational database model that was able to show the relationships between the application's main models/entities. In summary, these entities are:

1. `users`
2. `areas`
3. `spaces`
4. `plantrecords`
5. `plants`

As shown in the ERD in R6 above, these entities/tables are related to one another through foreign keys. Each entity also has its own attributes and data types, and importantly, each entity has an `id` primary key that is able to uniquely identity that table. This `id` is a serialised integer.

A thorough normalisation process was conducted to prevent redundancies or inconsistent dependencies. There are three rules for database normalisation and all of these rules were applied in the development of the database schema:

1. To satisfy first normal form (1NF), the tables must only contain single or atomic attributes of the same data type, every attribute must be unique, and the order in which data is stored is irrelevant (*First Normal Form*).
2. To satisfy second normal form (2NF), the table must be in 1NF and be reduced to a single purpose. All the columns must directly relate to the primary key of the table (*Description of the database normalization basics*).
3. To satisfy third normal form (3NF), the table must be in 2NF and any transitively dependent fields — that is, fields that depend on another field — must be eliminated (*Third Normal Form*). These transitively dependent attributes would need to be moved into a new table so they only depend on the primary key of that new table.

![UsersModel](docs/usersmodel.png)

The `users` table stores data about active users of the application, including their basic credentials for login and authentication purposes. The API requires users to enter a `f_name`, `l_name`, `email` and `password`. There is also an optional attribute, `is_admin`, a Boolean that will default to `False` if not provided. If `is_admin`, the user will have greater privileges in the application. In the development of the application, it was decided that a `users` model was important as it would allow for a unique user to input their own data related to their gardens. It proved to be an essential entity in the relational model as every table has `user_id` as a foreign key. This was particularly helpful in establishing nested fields usings `fields.Nested` in the Marshmallow schemas of each model. The server response could then show additional relational information in the JSON when accessing particular endpoints.

![AreasModel](docs/areasmodel.png)

The `areas` table was developed to enable a user to enter details regarding their broader planting areas; namely, its `name` as a 100-character string, as well as two Booleans indicating whether the area is outdoors or indoors: `is_outdoor` and `is_indoor`. It is broad enough to accommodate a wide range of city and more rural lifestyles. Examples of `areas` might be 'Front Yard', 'Back Yard', 'House', or 'Side of House'. This model structure was chosen to enable users to better filter their areas according to their needs. The `areas` model is in direct relationship with the `spaces` model. Ultimately, an urban user might only have one `area` associated with their `user_id`, perhaps 'Apartment'. However, a larger property owner will appreciate the greater flexibility afforded by the `area` model, specifically being able to break their property up into spaces. The `area` model could have been removed entirely and the responsibility could have completely fallen to the `spaces` model; however, that would be a less organised solution. One of the chief aims of this application is to enable a user to organise and plan their garden spaces. Ultimately, garden spaces can belong to different areas of a property.

![SpacesModel](docs/spacesmodel.png)

The `spaces` table was designed to enable users to set up their specific planting locations or spaces. Examples might be 'Vegetable Garden', 'Front Left Window', 'Front Right Window', 'Rose Garden', 'Alfresco' or 'Patio'. This is the heart of the application as this is the model that directly relates to the individuals plants or trees of the user, which is seen with its primary key, `space_id`, being in the `plants` model. A `space` is simply a smaller area within a broader `area`.

![PlantRecordsModel](docs/plantrecordsmodel.png)

The `plantrecords` table acts as a compendium or glossary of all the plant records logged by a particular user. The only mandatory field, other than the primary key of `plantrecord_id` is the `name` field. However, the API provides the user with plenty of scope to add information as they desire, including `description`, `preferred_location`, `water_rate`, `fertilisation_rate`, and `other_comments`. This is the data center of the application where, at any point, a user can log plant details as a record or place of safe keeping. Indeed, the `plantrecord` does not actually need to be linked to an actual `plant` garden - the model allows the user to simply enter into plant details as they desire. Perhaps they are in the process of planning out their garden and are not ready to commit to actually planting anything - this model allows the user to do this. However, ultimately a `plantrecord` will be related to a `plant` which, in essence, is like an instance of a plantrecord.

![PlantsModel](docs/plantsmodel.png)

As previously stated, the `plants` table is best considered as an instance of a `plantrecord`. It is a join table to facilitate a many to many relationship between `plantrecords` and `spaces` because ultimately a `plantrecord` can belong to many different `spaces`, but a space can also contain many different `plantrecords`. A many to many relationship such as this cannot be directly modelled in a database; therefore, a join table, `plants` was developed. A `plantrecord`, for example a 'Rose', can belong to many different `plants` or instances; however, that plant can only belong to one `plantrecord.` In other words, a rose can only ever be a rose, but many different rose bushes can ultimately be planted in a space.

## R10 - Project Management

## Works Cited

*Advantages of Database Management System (DBMS)*, Java T Point, https://www.javatpoint.com/advantages-of-dbms. Accessed 28 June 2023.

*Benefits of relational databases*, IBM, https://www.ibm.com/topics/relational-databases#:~:text=The%20primary%20benefit%20of%20the,group%2C%20and%20also%20combine%20queries. Accessed 28 June 2023.

*Data Schema*, APIFlask, https://apiflask.com/schema/. Accessed 1 June 2023.

*Description of the database normalization basics*, Microsoft, https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description. Accessed 28 June 2023.

*First Normal Form (1NF)*, Geeks for Geeks, https://www.geeksforgeeks.org/first-normal-form-1nf/. Accessed 1 July 2023.

*marshmallow: simplified object serialization*, readthedocs, https://marshmallow.readthedocs.io/en/stable/. Accessed 1 July 2023.

*Password Hashing with Bcrypt in Flask*, Geeks for Geeks, https://www.geeksforgeeks.org/password-hashing-with-bcrypt-in-flask/. Accessed 1 July 2023.

*SQLAlchemy 2.0 Documentation*, SQLAlchemy, https://docs.sqlalchemy.org/en/20/orm/quickstart.html. Accessed 28 June 2023.

*The benefits of PostgreSQL*, Prisma's Data Guide, https://www.prisma.io/dataguide/postgresql/benefits-of-postgresql. Accessed 28 June 2023.

*The Python SQL Toolkit and Object Relational Mapper*, SQLAlchemy, https://www.sqlalchemy.org. Accessed 28 June 2023.

*Third Normal Form*, Geeks for Geeks, https://www.geeksforgeeks.org/third-normal-form-3nf/. Accessed 1 July 2023.

*Understanding Object-Relational Mapping*, altexsoft, https://www.altexsoft.com/blog/object-relational-mapping/. Accessed 28 June 2023.

*What is a database management system?* IBM, https://www.ibm.com/docs/en/zos-basic-skills?topic=zos-what-is-database-management-system. Accessed 28 June 2023.

*What is PostgreSQL?* LinkedIn, https://www.linkedin.com/pulse/what-postgresql-introduction-advantages-disadvantages-ankita-sharda. Accessed 28 June 2023.