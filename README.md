<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to start](#how-to-start)
- [Defining context, containers, components, relationships](#defining-context-containers-components-relationships)
- [Usage](#usage)
  * [Generate architecture diagram](#generate-architecture-diagram)



<!-- INTRODUCTION -->
## Introduction

This package allows you to document your software architecture in C4 model. Key features include:

- Documentation of architecture in code
- Generation of architecture diagram

<!-- REQUIREMENTS -->
## Requirements

- python >= 3.0
- pyvenv

<!-- INSTALLATION -->
## Installation


* Git clone this repository and run make

```
make
```

<!-- HOW TO START -->
## How to start

To start the service, use:

```
source .venv/bin/activate
```


## Defining context, containers, components, relationships

Let's consider a simple example of describing the backend system of an online shop.



**1. Level: Context**

To document the Context, create Context, Person, System.
Afterwards add Person and System to context.

```
from c4.architecture import Context, Person, System, Container, Component

online_shop = Context(
    name='Online shop',
    description='E commerce online shop.')

external_user = Person(
    name='External users',
    description='Visitors of the online shop.')

online_shop.add_person(external_user)

backend = System(
    name='Shop backend',
    description='The php backend system of the online shop.'
)

external_system = System(
    name='External system',
    description='A example external system',
    internal=False
)

online_shop.add_system(backend)
```

**2. Level: Container**

Create Container and add container to the System:

```
product_management = Container(
    name='Product management',
    description='Management of products and catalogs.')

customer_management = Container(
    name='Customer management',
    description='Management of clients.')

db = Container(
    name='Backend database',
    description='Postgres database storing products and customer data.')

backend.add_container(customer_management)
backend.add_container(product_management)
backend.add_container(db)
```

**3. Level: Component**

Create Component and add Component to Container:

```
product_content = Component(
    name='Product content',
    description='Management of product content, e.g. image, price.')

product_inventory = Component(
    name='Product inventory',
    description='Management of stocks and logistic of products.')

product_management.add_component(product_content)
product_management.add_component(product_inventory)
```

**Relationship**

The relationship can be defined between Person, System, Container, Component.

```
external_user.add_relationship(backend, 'Makes requests', 'HTTPS')
backend.add_relationship(external_system, 'Uses', 'API')
```


## Usage

### Generate architecture diagram

Generating the architecture diagram from e.g. dwh.py with:

```
python3 architectures/dwh.py
```





