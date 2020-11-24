from c4.architecture import Context, Person, System, Container, Component

dwh = Context(
    name='Data Warehouse',
    description='Data warehouse integrating different data sources and monitoring business performance.')

internal_user = Person(
    name='Internal users',
    description='Employees in the organisation.')

dwh.add_person(internal_user)

dwh_app = System(
    name='DWH application',
    description='System running data pipelines (integrating, consolidating and transforming data).')

metabase = System(
    name='Metabase dashboards',
    description='Frontend BI application.')

dwh.add_system(dwh_app)
dwh.add_system(metabase)

pipelines = Container(
    name='Data pipelines',
    description='ETL (Extract, transform, load) pipelines.')

etl_db = Container(
    name='ETL database',
    description='Postgres database storing the data for ETL jobs.')

scheduler = Container(
    name='Scheduler',
    description='Jenkins service to schedule the run of pipelines.')

dwh_app.add_container(pipelines)
dwh_app.add_container(etl_db)
dwh_app.add_container(scheduler)

frontend_db = Container(
    name='Frontend database',
    description='Postgres database storing report ready data.')

metabase.add_container(frontend_db)

schema_management = Component(
    name='Schema management',
    description='Definition of schema and metabase in DWH.')

artifacts_generation = Component(
    name='Generation of artifacts',
    description='Automatic generation of artifacts in the ETL pipeline.')

pipelines.add_component(schema_management)
pipelines.add_component(artifacts_generation)

internal_user.add_relationship(dwh_app, 'Makes requests', 'HTTPS')
etl_db.add_relationship(frontend_db, 'Copies data to', 'JDBC')
scheduler.add_relationship(pipelines, 'Triggers')
pipelines.add_relationship(etl_db, 'Writes to')

from c4.graph import c4_graph

c4_graph(dwh)