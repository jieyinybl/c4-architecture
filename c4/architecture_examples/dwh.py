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

dwh_container = Container(
    name='DWH',
    description='DWH.')

postgres = Container(
    name='PostgreSQL',
    description='Database storing the data for ETL jobs.')

dwh_app.add_container(dwh_container)
dwh_app.add_container(postgres)

pipelines = Component(
    name='Pipelines',
    description='ETL (Extract, transform, load) pipelines.')

scheduler = Component(
    name='Scheduler',
    description='Scheduling ETL jobs.')

dwh_container.add_component(pipelines)
dwh_container.add_component(scheduler)


internal_user.add_usage(dwh_app, 'Makes requests')
dwh_app.add_usage(metabase, 'Copies data to')
#system2.add_usage(invoice_extractor_application, 'Updates records')
#ocr.add_usage(model, 'Sends OCR output in XML')
#