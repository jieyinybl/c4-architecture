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

product_content = Component(
    name='Product content',
    description='Management of product content, e.g. image, price.')

product_inventory = Component(
    name='Product inventory',
    description='Management of stocks and logistic of products.')

product_management.add_component(product_content)
product_management.add_component(product_inventory)

external_user.add_relationship(backend, 'Makes requests', 'HTTPS')
backend.add_relationship(external_system, 'Uses', 'API')

from c4.graph import c4_graph

c4_graph(online_shop, filename='onlineshop')